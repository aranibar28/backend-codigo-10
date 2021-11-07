from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from core.models import Booking
from core.serializers import BookingsSerializer, UserLoginSerializer

class BookingViewSet(viewsets.ViewSet):
    """API de Reservas"""
    def list(self, request):
        print(request.user)
        bookings = Booking.objects.all()
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data)

    # Por corregir
    def create(self, request):
        data = request.databases
        if not request.user.is_anonymous():
            data['user_id'] = request.user.id

        serializer = BookingsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        else:
            return Response(serializer.errors) 

class UserViewSet(viewsets.ViewSet):
    def login(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user, token = serializer.save()
            data = {
                'user': user.first_name,
                'access_token': token
            }
            return Response(data)
        else:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
