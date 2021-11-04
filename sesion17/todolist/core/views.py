from django.shortcuts import render, redirect
from django.views import View
from core.models import Task
from core.forms import TaskModelForm

# Create your views here.
class TasksView(View):
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

class TaskView(View):
    def get(self, request, pk):
        task = Task.objects.get(pk = pk)
        # form = TaskForm(initial={'title':task.title, 'description':task.description})
        form = TaskModelForm(instance = task)
        context = {
            'task': task,
            'form': form,
        }
        return render(request, "edit.html", context)

    def post(self, request, pk):
        task = Task.objects.get(pk = pk)
        data = request.POST
        task.title = data['title']
        task.description = data['description']
        task.due_date = data['due_date']
        task.save()
        return redirect('/tasks/')