from django.shortcuts import render, redirect
from django.views import View
from core.models import Task

# Create your views here.
class TaskView(View):
    def get(self, request):
        tasks = Task.objects.all()
        context = {
            "tasks": tasks,
        }
        return render(request, "index.html", context)

    def post(self, request):
        data = request.POST
        task = Task(title=data['title'])
        task.save()
        return redirect('/tasks/')