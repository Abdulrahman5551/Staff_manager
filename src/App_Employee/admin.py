from django.contrib import admin
from .models import Contact, Employee, Department, Compensation
# Register your models here.

admin.site.register(Contact)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Compensation)
