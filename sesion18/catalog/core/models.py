from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here. (GENERIC)  
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    sku = models.CharField(max_length=11)
    exp_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=CASCADE)
