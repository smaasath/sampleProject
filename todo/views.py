from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from .serializer import TaskSerializer
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class TaskView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk:
            try:
                tasks = Task.objects.get(id=pk)
                serializer = TaskSerializer(tasks, many=False)
                return Response(serializer.data, status=status.HTTP_200_OK)

            except Task.DoesNotExist:
                return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            tasks = Task.objects.all()
            serializer = TaskSerializer(tasks, many=True)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK);

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Task added successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            task = Task.objects.get(id=pk)
            serializer = TaskSerializer(instance=task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Task edited successfully"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            task = Task.objects.get(id=pk)
            task.delete()
            return Response({"message": "Task deleted successfully"}, status=status.HTTP_200_OK)

        except Task.DoesNotExist:
            return Response({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)
