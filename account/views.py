from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def top(request):
    return render(request, "account_setting.html")

def topRedirect(request):
    return redirect("top")