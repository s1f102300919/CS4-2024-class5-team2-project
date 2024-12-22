from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'authtest/home.html', {})

@login_required
def private_page(request):
    return render(request, 'record/index.html', {})

#今は使っていない
def public_page(request):
    return render(request, 'authtest/public.html', {})