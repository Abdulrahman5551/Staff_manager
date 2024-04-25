from django.shortcuts import render, redirect, get_object_or_404
from .forms import  DepartmentModelForm,CreateContactEmployeeModelForm,CreateEmployeeModelForm,UpdateContactEmployeeModelForm,UpdateEmployeeModelForm
from .models import *
from django.contrib import messages

# Create your views here.

def index(request):
    context = {
        'title': 'Index Page',
    }
    return render(request, 'App_Employee\index.html', context)

def dashboard(request):
    employees = Employee.objects.all()
    departments = Department.objects.all()
    print(employees.count())
    context = {
        'title': 'Dashboard Page',
        'employees': employees,
        'departments': departments,
    }
    return render(request, 'App_Employee\\Employees\\dashboard.html', context)

def create_contact(request):
    form_contact = CreateContactEmployeeModelForm()
    form_employee = CreateEmployeeModelForm()

    if request.method == "GET":
        context = {
            'form_contact': form_contact,
            }
        return render(request, 'App_Employee\\Employees\\create_contact_employee.html', context)
    
    elif request.method == "POST":
        print("Contact POST PASS ...")
        form_contact = CreateContactEmployeeModelForm(request.POST)
        if form_contact.is_valid():
            form_employee = CreateEmployeeModelForm()
            data = form_contact.save(commit=False)
            data.save()
            context = {
                'form_employee': form_employee,
                }
            return render(request, 'App_Employee\\Employees\\create_employee.html', context)
        else:
            print("Contact POST no PASS !!")
    
    context = {
        'formContact': CreateContactEmployeeModelForm(request.POST),
        }
    return render(request, 'App_Employee\\Employees\\create_contact_employee.html', context)


def create_employee(request):
    if request.method == "GET":
        form_employee = CreateEmployeeModelForm()
        context = {
            'form_employee': form_employee,
        }
        return render(request, 'App_Employee\\Employees\\create_employee.html', context)
    
    elif request.method == "POST":
        form_employee = CreateEmployeeModelForm(request.POST)
        if form_employee.is_valid():
            print("Employee POST PASS ...")
            data_employee = form_employee.save(commit=False)
            data_employee.save()
        
        else:
            print("Employee POST no PASS !!")
            form_employee = CreateEmployeeModelForm(request.POST)
            context = {
                'form_employee': form_employee,
            }
            return render(request, 'App_Employee\\Employees\\create_employee.html', context)
    
    return redirect('dashboard')
    
            

def details_employee(request, id):
    employeeData = get_object_or_404(Employee, pk=id)
    print(employeeData.salary)

    if request.method == "GET":
        context = {
            'title': 'Details Employee',
            'employeeData': employeeData,
    }
    return render(request, 'App_Employee\\Employees\\details_employee.html', context)
def departments(request):
    departments = Department.objects.all()
    context = {
        'title': 'Departments Page',
        'departments': departments,
    }
    return render(request, 'App_Employee\\Department\\departments.html', context)

def add_department(request):
    if request.method == "GET":
        form = DepartmentModelForm()
        context = {
            'title': 'Add Department',
            'form': form,
        }
        return render(request, 'App_Employee\\\Department\\add_department.html', context)
    
    else:
        form = DepartmentModelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('department')

def details_department(request, id):
    department = get_object_or_404(Department, pk=id)
    for data in department.employee_set.all():
        print(data.id)
    context = {
        'title': 'Details Department',
        'department': department,
    }
    return render(request, 'App_Employee\\\Department\\details_department.html', context)

def edit_department(request, id):
    dp = Department.objects.get(pk=id)
    
    if request.method == "GET":
        form = DepartmentModelForm(instance=dp)
        context = {
            'title': 'Edit Department',
            'form': form,
            }
        return render(request, 'App_Employee\\\Department\\edit_department.html', context)
    
    else:
        form = DepartmentModelForm(request.POST, instance=dp)
        if form.is_valid():
            form.save()
            print("Save ..")
            return redirect('department')

def delete_department(request, id):
    department = get_object_or_404(Department, pk=id)
    if request.method == "GET":

        context = {
            'title': 'Delete Department',
            'department': department
            }
        return render(request, 'App_Employee\\\Department\\delete_department.html', context)
    else:
        department.delete()
        print("delete ..")
        return redirect('department')

def remove_employee_from_department(request, id):
    departments = Department.objects.all()

    if request.method == "GET":
        context = {
            'title': 'Departments Page',
            'departments': departments,
            }
        return render(request, 'App_Employee\\Department\\confirm_remove_employee.html', context)
    
    else:

        employee = Employee.objects.get(pk=id)
        employee.department = None
        employee.save()
        messages.success(request, 'Remove Employee successfully...')
        return redirect('department')


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