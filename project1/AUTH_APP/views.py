from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def registerView(request):
    form = UserCreationForm()
    template_name = 'auth/register.html'
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    context = {'form': form}
    return render(request, template_name, context)

def loginView(request):
    template_name = 'auth/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        eml = request.POST.get('e')

        user = authenticate(username=un, password=pw)
        if user is not None:
            login(request,user)
            return redirect('showstu_url')
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login_url')