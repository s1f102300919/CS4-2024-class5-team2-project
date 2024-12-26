from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html', {})

@login_required
def private_page(request):
    return render(request, 'record/index.html', {})

#今は使っていない
def public_page(request):
    return render(request, 'authtest/public.html', {})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authtest/register.html',{'form':form})