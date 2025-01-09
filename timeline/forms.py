from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'time', 'comment']
    
    time = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'HH:MM'}))
    
    def clean_time(self):
        time_str = self.cleaned_data['time']
        # 'HH:MM'形式での入力を確認
        try:
            hours, minutes = map(int, time_str.split(':'))
            if hours < 0 or minutes < 0 or minutes >= 60:
                raise forms.ValidationError("無効な時間形式です。")
            # 時間と分の形式をそのまま文字列で返す
            return f"{hours:01}:{minutes:02}"  # 2桁の分を表示するための処理
        except ValueError:
            raise forms.ValidationError("時間は「HH:MM」の形式で入力してください。")
