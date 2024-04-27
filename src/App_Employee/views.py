from django.shortcuts import render, redirect, get_object_or_404
from .forms import  CreateDepartmentModelForm,CreateContactEmployeeModelForm,CreateEmployeeModelForm,UpdateContactEmployeeModelForm,UpdateEmployeeModelForm,UpdateDepartmentEmployeeForm
from .models import *
from django.contrib import messages
from django.utils import timezone
import datetime
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

def update_employee(request, id):
    employee_data = get_object_or_404(Employee,pk=id)

    if request.method == "GET":
        print("Update Employee GET Pass ..")
        employee_form = UpdateEmployeeModelForm(instance=employee_data)
        contact_form = UpdateContactEmployeeModelForm(instance=employee_data.contact)
        context = {
            'employee_data': employee_data,
            'employee_form' : employee_form,
            'contact_form': contact_form,
        }
        return render(request, 'App_Employee\\Employees\\update_employee.html', context)
    
    elif request.method == "POST":
        employee_form = UpdateEmployeeModelForm(request.POST, instance=employee_data)
        contact_form = UpdateContactEmployeeModelForm(request.POST, instance=employee_data.contact)

        if employee_form.is_valid() and contact_form.is_valid():
            data_employee = employee_form.save(commit=False)
            data_contact = contact_form.save(commit=False)

            data_employee.save()
            data_contact.save()
            print("Update Employee and Contact Done ..")
        
        else:

            context = {
                'employee_form' : UpdateEmployeeModelForm(request.POST, instance=employee_data),
                'contact_form' : UpdateContactEmployeeModelForm(request.POST, instance=employee_data.contact)
            }

            return render(request, 'App_Employee\\Employees\\update_employee.html', context)
        print("Update Employee POST Pass ..")
    
    return redirect('details-employee', id=employee_data.id)

def delete_employee(request, id):
    employee_data = get_object_or_404(Employee,pk=id)

    if request.method == "GET":
        context = {
            'employee_data': employee_data,
            }

        return render(request, 'App_Employee\\Employees\\delete_employee.html', context)
    
    elif request.method == "POST":
        employee_data.delete()
        context = {
            'employee_data': employee_data,
            }

        return render(request, 'App_Employee\\Employees\\confirm_delete_employee.html', context)
    
    return redirect('dashboard')

def departments(request):
    departments = Department.objects.all()
    context = {
        'title': 'Departments Page',
        'departments': departments,
    }
    return render(request, 'App_Employee\\Department\\departments.html', context)

def create_department(request):
    if request.method == "GET":
        form = CreateDepartmentModelForm()
        context = {
            'title': 'Add Department',
            'form': form,
        }
        return render(request, 'App_Employee\\\Department\\create_department.html', context)
    
    else:
        form = CreateDepartmentModelForm(request.POST)
        if form.is_valid():
            print("pass ..")
            form.save()
            return redirect('departments')
        
        else:
            print("no pass !!")
            context = {
                'form': CreateDepartmentModelForm(request.POST),
            }
            return render(request, 'App_Employee\\\Department\\create_department.html', context)

def details_department(request, id):
    department = get_object_or_404(Department, pk=id)

    context = {
        'title': 'Details Department',
        'department': department,
    }
    return render(request, 'App_Employee\\\Department\\details_department.html', context)

def update_department(request, id):
    department = Department.objects.get(pk=id)
    
    if request.method == "GET":
        form = UpdateDepartmentEmployeeForm(instance=department)
        context = {
            'title': 'Edit Department',
            'form': form,
            }
        return render(request, 'App_Employee\\\Department\\update_department.html', context)
    
    else:
        form = UpdateDepartmentEmployeeForm(request.POST, instance=department)
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
        context = {
            'title': 'Confirm Department Delete',
            }
        return render(request, 'App_Employee\\\Department\\confirm_delete_department.html', context)

def joining_department(request, id):
    department = Department.objects.get(pk=id)
    employees = Employee.objects.all().filter(is_department=False)

    if request.method == "GET":
        context = {
        'title': 'Details Department',
        'department': department,
        'employees': employees,
        }
        return render(request, 'App_Employee\\\Department\\joining_employees.html', context)
    
    elif request.method == "POST":
        empID = request.POST.get('empID')
        employee = Employee.objects.get(pk=empID)
        employee.department = department
        employee.is_department = True
        employee.join_department_date = datetime.datetime.now()
        employee.save()

    return redirect('departments')


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
