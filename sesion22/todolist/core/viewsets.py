from rest_framework import serializers, viewsets
from rest_framework.response import Response 
from core.serializers import UserLoginSerializer, TaskSerializer
from core.models import Task

class UserViewSet(viewsets.ViewSet):
    def login(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid():
            user, token = serializer.save()
            data = {
                'username': f'{user.first_name} {user.last_name}',
                'access_token': token
            }
            return Response(data)
        else:
            return Response(serializer.errors)

class TasksViewSet(viewsets.ViewSet):
    def list(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
