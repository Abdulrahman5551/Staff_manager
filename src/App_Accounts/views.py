from django.shortcuts import render, redirect, get_object_or_404
from .forms import LoginForm, RegisterForm, UpdateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
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
    
def profile(request, id):
    user = get_object_or_404(User, pk=id)

    if request.method == "GET":
        context = {
            'user': user,
        }
        return render(request, 'App_Accounts//profile.html', context)

def update_profile(request, id):
    user = get_object_or_404(User, pk=id)

    if request.method == "GET":
        profile_form = UpdateUserForm(instance=user)

        context = {
            'profile_form': profile_form,
        }

        return render(request, 'App_Accounts//update_profile.html', context)
    
    elif request.method == "POST":
        profile_form = UpdateUserForm(request.POST, instance=user)

        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile-user', id=user.id)
        
        else:

            context = {
                'profile_form': UpdateUserForm(request.POST, instance=user),
            }

            return render(request, 'App_Accounts//update_profile.html', context)