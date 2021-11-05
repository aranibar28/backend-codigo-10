from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    sku = models.CharField(max_length=11)
    exp_date = models.DateField()
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    