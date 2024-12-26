from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        labels = {
            'username': 'ユーザー名（任意の文字列を入力してください）',
            'password1': 'パスワード（安全なものを設定してください）',
            'password2': 'パスワード（確認用）',
        }
        help_texts = {
            'username': '※ 150文字以内、英数字と @/./+/-/_ のみ使用可能',
            'password1': '※ 8文字以上で、よく使われるものを避けてください',
        }
        error_messages = {
            'username': {
                'required': 'ユーザー名を入力してください。',
                'max_length': '150文字以内で入力してください。',
            },
            'password1': {
                'required': 'パスワードを入力してください。',
            },
        }
