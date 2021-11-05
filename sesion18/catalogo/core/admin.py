from django.contrib import admin
from core.models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)