from django.shortcuts import render, redirect
from .forms import EmployeeForm, DepartmentModelForm
from .models import *

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
        departments = Department.objects.all()
        context = {
            'title': 'Add Employee',
            'form': form,
            'departments': departments,
        }
        return render(request, 'App_Employee\\add_employee.html', context)
    
    else:
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        gender = request.POST.get('gender')
        birth_date = request.POST.get('birthdate')
        print(birth_date)
        salary = request.POST.get('salary_select')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        dp = request.POST.get('department_select')
        get_department = Department.objects.get(name=dp)

        new_contact = Contact.objects.create(
            phone=phone, email=email, address=address, city=city
        )


        employee = Employee.objects.create(
            first_name=fn, last_name=ln, gender=gender, birth_date=birth_date,
            salary=salary, contact=new_contact, department=get_department
        )
        print("Save ..")
        return redirect('dashboard')

def departments(request):

    context = {
        'title': 'Departments Page',
    }
    return render(request, 'App_Employee\departments.html', context)

def add_department(request):
    if request.method == "GET":
        form = DepartmentModelForm()
        context = {
            'title': 'Add Department',
            'form': form,
        }
        return render(request, 'App_Employee\\add_department.html', context)
    
    else:
        form = DepartmentModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('department')

def details_department(request):
        context = {
            'title': 'Details Department',
        }
        return render(request, 'App_Employee\\details_department.html', context)

def edit_department(request, id):
    if request.method == "GET":
        dp = Department.objects.get(pk=id)
        form = DepartmentModelForm(request.POST, instance=dp)
        context = {
            'title': 'Edit Department',
            'form': form,
            }
        return render(request, 'App_Employee\\edit_department.html', context)

def delete_department(request, id):

        context = {
            'title': 'Delete Department',
            }
        return render(request, 'App_Employee\\delete_department.html', context)


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