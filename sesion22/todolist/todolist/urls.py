from django.contrib import admin
from django.urls import path
from core.viewsets import UserViewSet, TaskViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', UserViewSet.as_view({
        'get': 'login',
    })),
    path('tasks/', TaskViewSet.as_view({
        'get': 'list',
        'post': 'create',
    })),
    path('task/<pk>', TaskViewSet.as_view({
       'put': 'update',
       'delete': 'destroy',
    }))
]
