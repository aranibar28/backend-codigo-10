from django.contrib import admin
from core.models import Booking

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'nro_mesa', 'fec_reserva', 'estado')
    list_filter = ('fec_reserva', 'estado')
    search_fields = ['estado']
    ordering = ('id',)

admin.site.register(Booking, BookingAdmin)