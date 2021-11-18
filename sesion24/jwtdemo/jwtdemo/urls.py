from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from core.viewsets import AuthViewSet, UserViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt_login/', AuthViewSet.as_view({
        'post': 'post',
    })),
    path('api/signup/', UserViewSet.as_view({
        'post': 'sing_up',
    })),
    path('api/users/', UserViewSet.as_view({
        'get': 'list',
    })),
    #path('api/user/<pk>/', UserViewSet.as_view({
    #    'get': 'retrieve',
    #})),
    path('api/user/me/', UserViewSet.as_view({
        'get': 'list',
    })),
]
