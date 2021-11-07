from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150)
    main_picture = models.ImageField(upload_to="categories/")

    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    main_picture = models.ImageField(upload_to="products/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
