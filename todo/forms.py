from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo', 'deadline', 'done']
        widgets = {
            'todo': forms.TextInput(attrs={'id': 'todo'}),
            'deadline': forms.DateInput(attrs={'type': 'date'}),
        }
