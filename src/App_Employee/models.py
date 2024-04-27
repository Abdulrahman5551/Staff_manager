from django.db import models

# Create your models here.
class Contact(models.Model):
    choice_city = [
        ('Riyadh', 'Riyadh'),
        ('Abha', 'Abha'),
        ('Al Bahah', 'Al Bahah'),
        ('Dammam', 'Dammam'),
        ('Jeddah', 'Jeddah'),
        ('Jizan', 'Jizan'),
        ('Mecca', 'Mecca'),
    ]
    phone = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(choices=choice_city, max_length=100)
    joined_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.phone

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Compensation(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    choice_gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    choices_salary = [
        ('5000', '5000'),
        ('8000', '8000'),
        ('10.000', '10.000'),
        ('12.000', '12.000'),
        ('15.000', '15.000'),
    ]
    creation_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=choice_gender, max_length=20)
    birth_date = models.DateField(null=True)
    salary = models.CharField(choices=choices_salary, max_length=100)
    
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    is_department = models.BooleanField(default=False)
    join_department_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)

    compensations = models.ManyToManyField(Compensation, null=True, blank=True)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
