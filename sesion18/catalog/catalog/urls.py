from django.contrib import admin
from django.urls import path
from core.viewsets import ProductViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('catalog/<pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy',
    }))
]
