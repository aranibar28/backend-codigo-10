from django.contrib import admin
from core.models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'subtitle', 'main_picture')

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)