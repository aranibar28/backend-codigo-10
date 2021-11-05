from django.contrib import admin
from core.models import Product, Category

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)

# Register your models here. (GENERIC)
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
