from django.contrib import admin
from core.models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category_name')

admin.site.register(Product, ProductAdmin)

# Register your models here. (GENERIC)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

admin.site.register(Category, CategoryAdmin)
