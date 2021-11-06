from rest_framework import viewsets
from rest_framework.response import Response
from core.models import Booking
from core.serializers import BookingsSerializer

class BookingViewSet(viewsets.ViewSet):
    def list(self, request):
        bookings = Booking.objects.all()
        serializer = BookingsSerializer(bookings, many=True)
        return Response(serializer.data)
