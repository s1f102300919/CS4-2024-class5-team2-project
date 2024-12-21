from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def top(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect('record.html')
    else:
        form = AuthenticationForm()
            
    return render(request, "account_setting.html")

def topRedirect(request):
    return redirect("top")

@login_required
def record(request):
    return render(request, "record.html")