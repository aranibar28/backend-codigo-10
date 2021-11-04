from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True)
    due_date = models.DateField(null=True)
    finished = models.BooleanField(null=True)
    