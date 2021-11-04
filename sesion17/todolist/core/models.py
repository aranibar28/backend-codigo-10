from django.db import models
from django.db.models.deletion import CASCADE

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
            return self.name

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    finished = models.BooleanField(null=True)
    attachments = models.ImageField(null=True, upload_to="attachments", blank=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, null=True)
    def __str__(self):
        return f"Title: {self.title}"

