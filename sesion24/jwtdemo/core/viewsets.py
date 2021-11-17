from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from core.serializers import UserSerializer, SignUpSerializer

class UserViewSet(ViewSet):
    def sing_up(self, request):
        data = request.data
        serializer = SignUpSerializer(data=data)

        if serializer.is_valid():
            user = serializer.save()
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class CustomObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["first_name"] = user.first_name
        token["last_name"] = user.last_name
        token["email"] = user.email
        return token

class AuthViewSet(ViewSet):
    def post(self, request):
        data = request.data
        email = data['email']
        password = data['password']

        user = User.objects.filter(email__exact=email).first()
        user_authenticated = authenticate(username=user.username, password=password)

        if user_authenticated != None:
            token = CustomObtainPairSerializer.get_token(user_authenticated)
            return Response({
                "status": "ok",
                "token": str(token.access_token),
            })
        else:
            return Response({
                "status": "error",
            })
