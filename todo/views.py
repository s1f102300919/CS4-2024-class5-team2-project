from django.shortcuts import render
from django.views.generic import ListView
from .models import Task

# Create your views here.
def record(request):
    return render(request, 'index.html')

def timeline(request):
    return render(request, 'timeline.html')

class TaskList(ListView):
    #使用するModelを指定
    model = Task
    #使用するテンプレートファイルを指定
    template_name = 'todo/task_list.html'
    #コンテキスト名を設定
    context_object_name = 'tasks'
    #データの並び順を指定
    ordering = ['-created_at', 'due_date']