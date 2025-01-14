from django.shortcuts import render

from .models import Task

# Create your views here.
def todo(request):
    tasks = Task.objects.all()
    print(tasks)
    return render(request, 'todo/todo.html', {tasks: tasks})

def delite(request):
    return render(request, 'todo.delite.html')

def record(request):
    return render(request, 'index.html')

def timeline(request):
    return render(request, 'timeline.html')