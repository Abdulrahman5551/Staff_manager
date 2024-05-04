from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# Create your views here.

def sign_in(request):
    if request.method == "GET":
        form = LoginForm()
        context = {
            'form': form,
        }
        return render(request, 'App_Accounts//login.html', context)
    
    elif request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)

                return redirect('index')
        context = {
            'form': LoginForm(request.POST),
            }
        return render(request, 'App_Accounts//login.html', context)

def sign_out(request):
    logout(request)
    return redirect('login')


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        context = {
            'form': form,
        }
        return render(request, 'App_Accounts//register.html', context)
    
    elif request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.title()
            user.save()
            login(request, user)
            return redirect('dashboard')
        context = {
            'form': RegisterForm(request.POST),
            }
        return render(request, 'App_Accounts//register.html', context)