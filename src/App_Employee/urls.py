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

]