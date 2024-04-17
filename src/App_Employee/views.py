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

def add_employee(request):
    context = {
        'title': 'Add Employee',
    }
    return render(request, 'App_Employee\\add_employee.html', context)

def departments(request):
    context = {
        'title': 'Departments Page',
    }
    return render(request, 'App_Employee\departments.html', context)

def add_department(request):
    context = {
        'title': 'Add Department',
    }
    return render(request, 'App_Employee\\add_department.html', context)


def compensations(request):
    context = {
        'title': 'Compensation Page',
    }
    return render(request, 'App_Employee\compensations.html', context)

def add_compensation(request):
    context = {
        'title': 'Add Compensation',
    }
    return render(request, 'App_Employee\\add_compensations.html', context)