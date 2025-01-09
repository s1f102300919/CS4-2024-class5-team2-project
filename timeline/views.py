from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

# カウントダウンページビュー
def countdown(request):
    return render(request, 'countdown.html')