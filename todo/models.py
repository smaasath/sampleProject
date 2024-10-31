from django.db import models


# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', 'TODO'),
        ('PROGRESS', 'PROGRESS'),
        ('COMPLETE', 'COMPLETE'),
    ]

    PRIORITY_CHOICES = [
        ('LOW', 'LOW'),
        ('MEDIUM', 'MEDIUM'),
        ('HIGH', 'HIGH'),
    ]
    task_title = models.CharField(max_length=255)
    description = models.TextField()
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)

    def __str__(self):
        return self.task_title
