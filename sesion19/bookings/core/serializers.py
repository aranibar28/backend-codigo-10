from rest_framework import serializers

class BookingsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nro_mesa = serializers.IntegerField()
    fec_reserva = serializers.DateTimeField()
    estado = serializers.CharField(max_length=100)
    