from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Index Page',
    }
    return render(request, 'App_Employee\index.html', context)

def dashboard(request):
    context = {
        'title': 'Dashboard Page',
    }
    return render(request, 'App_Employee\dashboard.html', context)