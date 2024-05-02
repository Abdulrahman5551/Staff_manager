from django.shortcuts import render, redirect, get_object_or_404
from .forms import  CreateDepartmentModelForm,CreateContactEmployeeModelForm,CreateEmployeeModelForm,UpdateContactEmployeeModelForm,UpdateEmployeeModelForm,UpdateDepartmentEmployeeForm, CreateCompensationModelForm, UpdateCompensationModelForm
from .models import *
from django.contrib import messages
from django.utils import timezone
import datetime
from django.db.models import Q
# Create your views here.

def index(request):
    context = {
        'title': 'Index Page',
    }
    return render(request, 'App_Employee\index.html', context)

# Dashboard : view All Employees and link Department and Compensation Pages
def dashboard(request):

    if request.method == "GET":
        employees = Employee.objects.all()
        departments = Department.objects.all()
        compensations = Compensation.objects.all()

        context = {
            'title': 'Dashboard Page',
            'employees': employees,
            'departments': departments,
            'compensations': compensations,
        }
        return render(request, 'App_Employee\\Employees\\dashboard.html', context)
    
    elif request.method == "POST":
        pass

def sort_dashboard(request, sort_by):
    if sort_by == "first_name":
        employees = Employee.objects.all().order_by(sort_by)
        departments = Department.objects.all()
        compensations = Compensation.objects.all()

        context = {
            'title': 'Dashboard Page',
            'employees': employees,
            'departments': departments,
            'compensations': compensations,
        }
        return render(request, 'App_Employee\\Employees\\dashboard.html', context)
    
    elif sort_by == '-first_name':
        employees = Employee.objects.all().order_by(sort_by)
        departments = Department.objects.all()
        compensations = Compensation.objects.all()

        context = {
            'title': 'Dashboard Page',
            'employees': employees,
            'departments': departments,
            'compensations': compensations,
        }
        return render(request, 'App_Employee\\Employees\\dashboard.html', context)
    
    elif sort_by == 'gender':
        employees = Employee.objects.all().order_by(sort_by)
        departments = Department.objects.all()
        compensations = Compensation.objects.all()

        context = {
            'title': 'Dashboard Page',
            'employees': employees,
            'departments': departments,
            'compensations': compensations,
        }
        return render(request, 'App_Employee\\Employees\\dashboard.html', context)
    
    elif sort_by == '-gender':
        employees = Employee.objects.all().order_by(sort_by)
        departments = Department.objects.all()
        compensations = Compensation.objects.all()

        context = {
            'title': 'Dashboard Page',
            'employees': employees,
            'departments': departments,
            'compensations': compensations,
        }
        return render(request, 'App_Employee\\Employees\\dashboard.html', context)
    return redirect('dashboard')
    


###############################################################################################

# -------- Contact -------------

def create_contact(request):
    # Create form Contact
    form_contact = CreateContactEmployeeModelForm()

    # Create form Employees
    form_employee = CreateEmployeeModelForm()

    if request.method == "GET":
        context = {
            'form_contact': form_contact, # Send Form Contact To Template
            }
        return render(request, 'App_Employee\\Employees\\create_contact_employee.html', context)
    
    elif request.method == "POST":

        # Get Data From Request and Sand To From Contact
        form_contact = CreateContactEmployeeModelForm(request.POST)

        if form_contact.is_valid():

            # Create Form Employees
            form_employee = CreateEmployeeModelForm()
            data = form_contact.save(commit=False)

            # Save Data Contact
            data.save()
            context = {
                'form_employee': form_employee, # Send Form Employee To Template
                }
            return render(request, 'App_Employee\\Employees\\create_employee.html', context)
        else:
            
            context = {
                'formContact': CreateContactEmployeeModelForm(request.POST),
                }
            return render(request, 'App_Employee\\Employees\\create_contact_employee.html', context)


###############################################################################################


# -------- Employee -------------
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



###############################################################################################


# -------- Department -------------
def departments(request):
    departments = Department.objects.all()
    employees_joined = Employee.objects.filter(is_department=True)

    context = {
        'title': 'Departments Page',
        'departments': departments,
        'employees_joined': len(employees_joined),
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
            data = form.save()
            messages.success(request, f'Create New Department "{data.name}" Successfully...')
            return redirect('departments')
        
        else:
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
            return redirect('details-department', id=department.id)
        
        else:
            print("Form error!!!")
            context = {
            'title': 'Edit Department',
            'form': form,
            }
            return render(request, 'App_Employee\\\Department\\update_department.html', context)
        
def delete_department(request, id):
    department = get_object_or_404(Department, pk=id)
    if request.method == "GET":

        context = {
            'title': 'Delete Department',
            'department': department,
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
    employee = Employee.objects.get(pk=id)
    department = employee.department
    if request.method == "GET":
        context = {
            'title': 'Departments Page',
            'department': department,
            'employee': employee,
            }
        return render(request, 'App_Employee\\Department\\confirm_remove_employee.html', context)
    
    else:

        employee.department = None
        employee.is_department = False
        print(employee.is_department)
        employee.save()
        messages.success(request, 'Remove Employee Successfully...')
        return redirect('details-department', id=department.id)



###############################################################################################


# -------- Compensations -------------
def compensations(request):
    compensations = Compensation.objects.all()
    employees_has_compensations = Employee.objects.all().filter(is_compensation=True)
    employees_no_has_compensations = Employee.objects.all().filter(is_compensation=False)

    if request.method == "GET":
        context = {
            'compensations' : compensations,
            'employees_has_compensations': employees_has_compensations,
            'employees_no_has_compensations': employees_no_has_compensations,
        }
        return render(request, 'App_Employee\\Compensations\\compensations.html', context)


# Create Compensations
def create_compensations(request):
    form = CreateCompensationModelForm()

    if request.method == "GET":

        context = {
            'form': form,
        }

        return render(request, 'App_Employee\\Compensations\\create_compensation.html', context)
    
    elif request.method == "POST":

        form = CreateCompensationModelForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Created a Reward...')
            return redirect('compensations')
        
        context = {
            'form': form,
        }

        return render(request, 'App_Employee\\Compensations\\create_compensation.html', context)


def update_compensation(request, id):
    compensation = Compensation.objects.get(pk=id)
    
    if request.method == "GET":
        form = UpdateCompensationModelForm(instance=compensation)
        context = {
            'titel': 'Edit Compensation',
            'form': form,
        }

        return render(request, 'App_Employee\\Compensations\\update_compensation.html', context)
    
    elif request.method == "POST":
        form = UpdateCompensationModelForm(request.POST, instance=compensation)

        if form.is_valid():
            form.save()
            return redirect('details-compensation', id=compensation.id)
        
        else:

            context = {
                'titel': 'Edit Compensation',
                'form': form,
            }

            return render(request, 'App_Employee\\Compensations\\update_compensation.html', context)


def delete_compensation(request, id):
    compensation = Compensation.objects.get(pk=id)

    if request.method == "GET":

        context = {
            'compensation': compensation,
        }

        return render(request, 'App_Employee\\Compensations\\delete_compensation.html', context)

    else:

        compensation.delete()
        return render(request, 'App_Employee\\Compensations\\confirm_delete_compensation.html')
    

def details_compensation(request, id):
    compensation = get_object_or_404(Compensation, pk=id)
    employee_has_compensation = compensation.employee_set.all()
    employee_no_has_compensation = Employee.objects.all().filter(~Q(compensations=compensation))


    if request.method == "GET":
        context = {
            'compensation': compensation,
            'employee_has_compensation' :employee_has_compensation,
            'employee_no_has_compensation': employee_no_has_compensation,
        }
        return render(request, 'App_Employee\\Compensations\\details_compensation.html', context)
    
    else:
        pass

def join_employee_in_compensations(request, copID, empID):
    compensation = Compensation.objects.get(pk=copID)
    employee = Employee.objects.get(pk=empID)
    full_name = employee.first_name +' '+ employee.last_name
    employee.compensations.add(compensation)
    employee.is_compensation = True
    employee.save()
    if request.method == "GET":
        messages.success(request, f"Add Employee: {full_name.title()} in Compensation {compensation.name.title()}")
        return redirect('details-compensation', id=compensation.id)


def remove_employee_in_compensations(request, copID, empID):
    compensation = Compensation.objects.get(pk=copID)
    employee = Employee.objects.get(pk=empID)
    full_name = employee.first_name +' '+ employee.last_name
    employee.compensations.remove(compensation)
    if employee.compensations.all().count() == 0:
        employee.is_compensation = False
    employee.save()
    messages.warning(request, f"Remove Employee: {full_name.title()} in Compensation {compensation.name.title()}")
    return redirect('details-compensation', id=compensation.id)