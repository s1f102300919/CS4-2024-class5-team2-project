from django.shortcuts import render

# Create your views here.
def record(request):
    return render(request, 'index.html')

def timeline(request):
    return render(request, 'timeline.html')

def todo(request):
    return render(request, 'todo.html')