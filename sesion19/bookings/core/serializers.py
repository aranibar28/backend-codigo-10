from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import password_validation, authenticate

class BookingsSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    nro_mesa = serializers.IntegerField()
    fec_reserva = serializers.DateTimeField()
    estado = serializers.CharField()
    nro_personas = serializers.IntegerField()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Las credenciales no son válidas')

        self.context['user'] = user
        return data

    def create(self, data):
        toke, create = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], toke.key
