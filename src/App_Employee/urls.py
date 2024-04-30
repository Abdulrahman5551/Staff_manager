from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('dashboard/', views.dashboard, name="dashboard"),

   # Employee & Contact
   path('create-contact-employee/', views.create_contact, name="create-contact-employee"),
   path('create-employee/', views.create_employee, name="create-employee"),
   path('details-employee/<int:id>/', views.details_employee, name="details-employee"),
   path('update-employee/<int:id>/', views.update_employee, name="update-employee"),
   path('delete-employee/<int:id>/', views.delete_employee, name="delete-employee"),

   # Department
   path('departments/', views.departments, name="departments"),
   path('create-department/', views.create_department, name="create-department"),
   path('details-department/<int:id>/', views.details_department, name="details-department"),
   path('update-department/<int:id>/', views.update_department, name="update-department"),
   path('delete-department/<int:id>/', views.delete_department, name="delete-department"),
   path('joining-department/<int:id>/', views.joining_department, name="joining-department"),
   path('remove-employee-department/<int:id>/', views.remove_employee_from_department, name="remove-employee-department"),

   # Compensations
   path('compensations/', views.compensations, name="compensations"),
   path('create-compensations/', views.create_compensations, name="create-compensations"),
   path('details-compensation/<int:id>/', views.details_compensation, name="details-compensation"),
   path('update-compensation/<int:id>/', views.update_compensation, name="update-compensation"),
   path('delete-compensation/<int:id>/', views.delete_compensation, name="delete-compensation"),

   path('get-employee-compensations/<int:id>/', views.get_employee_compensation, name="get-employee-compensations"),

]