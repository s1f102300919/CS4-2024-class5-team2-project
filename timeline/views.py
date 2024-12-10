from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'timeline/home.html',{})