from django.contrib import admin
from core.models import Booking

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Booking, CategoryAdmin)