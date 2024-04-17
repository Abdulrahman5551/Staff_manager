from django.shortcuts import render, redirect
from .forms import EmployeeForm

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
    
    if request.method == "GET":
        form = EmployeeForm()
        context = {
            'title': 'Add Employee',
            'form': form,
        }
        return render(request, 'App_Employee\\add_employee.html', context)
    
    else:
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        g = request.POST.get('gender')
        bd = request.POST.get('birthday')
        sa = request.POST.get('salary_select')
        print(ln)
        print(g)
        print(bd)
        print(sa)
        return redirect('dashboard')

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