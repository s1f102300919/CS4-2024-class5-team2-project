from django.shortcuts import render, redirect
from django.views.generic import ListView, UpdateView
from django.views import View
from django.urls import reverse_lazy
from django.forms import DateInput
from .models import Task
from .forms import TaskForm

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

    def get_context_data(self, **kwargs):
        #1コンテキストの取得
        context = super().get_context_data(**kwargs)
        #2コンテキストのフォームをセット
        context['form'] = TaskForm()
        return context
    
class TaskCreate(View):
    #送信されたフォーム内容のデータベース処理
    def post(self, request):
        #1送信データのチェック
        form = TaskForm(request.POST)
        #2問題がなければ登録
        if form.is_valid():
            task = form.save()
        #3タスク一覧へ遷移
        return redirect('task_list')
    
#1.UpdateViewで作成
class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'due_date']
    template_name = 'todo/task_edit.html'
    #2.成功時URLを指定
    success_url = reverse_lazy('task_list')
 
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        #3.due_dateフィールドのウィジェットを上書き
        form.fields['due_date'].widget = DateInput(attrs={'type': 'date'})
        return form