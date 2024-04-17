from django import forms

class EmployeeForm(forms.Form):
    choice_gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    first_name = forms.CharField(max_length=100, label='First Name')
    last_name = forms.CharField(max_length=100, label='Last Name')
    gender = forms.ChoiceField(choices=choice_gender, label='Gender')
    birth_date = forms.DateField(label='Birth Day')
    salary = forms.IntegerField(label='Salary')
    phone = forms.CharField(max_length=100, label='Phone Number')
    email = forms.CharField(max_length=100, label='Email')
    address = forms.CharField(max_length=255, label='Address')
    city = forms.CharField(max_length=100, label='City')