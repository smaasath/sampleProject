# Generated by Django 5.0 on 2024-10-31 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='start_date',
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')], max_length=6),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TODO', 'TODO'), ('PROGRESS', 'PROGRESS'), ('COMPLETE', 'COMPLETE')], max_length=8),
        ),
    ]