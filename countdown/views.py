from django.shortcuts import render

# カウントダウンページビュー
def countdown(request):
    return render(request, 'countdown.html')
