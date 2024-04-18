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

    def __str__(self):
        return self.phone

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Employee(models.Model):
    choice_gender = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=choice_gender, max_length=50)
    birth_date = models.DateField()
    salary = models.IntegerField(default=1000)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
