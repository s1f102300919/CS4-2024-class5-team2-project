from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    #1HTMLの入力フィールドをカレンダーに変換
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)

    #2フォームに対応するModelとフィールドを指定する
    class Meta:
        model = Task
        fields = ('title', 'due_date')