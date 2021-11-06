from django.db import models

# Create your models here.
class Booking(models.Model):
    nro_mesa = models.IntegerField(null=True)
    fec_reserva = models.DateTimeField(null=True)
    estado = models.CharField(max_length=100, null=True)
