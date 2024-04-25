from django import forms
from django.forms.widgets import NumberInput
from .models import Department, Employee, Contact


class DepartmentModelForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'

class UpdateDepartmentEmployeeForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('name',)
    

class CreateContactEmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('phone','email','address','city','active')

class UpdateContactEmployeeModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('phone','email','address','city')

        widgets = {
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.Select(attrs={'class':'form-control'}),
        }

class CreateEmployeeModelForm(forms.ModelForm):
    choices_salary = (
        ('5000', '5000'),
        ('8000', '8000'),
        ('10.000', '10.000'),
        ('12.000', '12.000'),
        ('15.000', '15.000'),
    )
    contact = forms.ModelChoiceField(queryset=Contact.objects.all().filter(active=True))
    birth_date= forms.DateField(widget = NumberInput(attrs={'type':'date'}), disabled=False)
    salary = forms.ChoiceField(choices=choices_salary)
    class Meta:
        model = Employee
        fields = ('first_name','last_name','gender','birth_date','salary','contact')

class UpdateEmployeeModelForm(forms.ModelForm):
    choices_salary = [
        ('1', '5000'),
        ('2', '8000'),
        ('3', '10.000'),
        ('4', '12.000'),
        ('5', '15.000'),
    ]
    class Meta:
        model = Employee
        fields = ('first_name','last_name','gender','birth_date','salary')
