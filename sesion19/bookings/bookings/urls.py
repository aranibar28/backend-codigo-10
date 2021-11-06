from django.contrib import admin
from django.urls import path
from core.viewsets import BookingViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bookings/', BookingViewSet.as_view({
        'get': 'list',
    }))
]
