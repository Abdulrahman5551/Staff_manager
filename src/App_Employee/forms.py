from django import forms
from .models import Department


class EmployeeForm(forms.Form):
    choice_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    choice_city = (
        ('Riyadh', 'Riyadh'),
        ('Abha', 'Abha'),
        ('Al Bahah', 'Al Bahah'),
        ('Dammam', 'Dammam'),
        ('Jeddah', 'Jeddah'),
        ('Jizan', 'Jizan'),
        ('Mecca', 'Mecca'),
    )
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    gender = forms.ChoiceField(choices=choice_gender, label='Gender')
    birth_date = forms.DateField(label='Birth Day')
    salary = forms.IntegerField(label='Salary')
    phone = forms.CharField(max_length=100, label='Phone Number')
    email = forms.CharField(max_length=100, label='Email')
    address = forms.CharField(max_length=255, label='Address')
    city = forms.ChoiceField(choices=choice_city, label='City')

class DepartmentModelForm(forms.ModelForm):
        class Meta:
            model = Department
            fields = '__all__'