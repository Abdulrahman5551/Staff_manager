from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('dashboard/', views.dashboard, name="dashboard"),
   path('create-employee/', views.add_employee, name="create-employee"),


   path('department/', views.departments, name="department"),
   path('create-department/', views.add_department, name="create-department"),
   path('details-department/', views.details_department, name="details-department"),
   path('edit-department/<int:id>/', views.edit_department, name="edit-department"),
   path('delete-department/<int:id>/', views.delete_department, name="delete-department"),

   path('compensation/', views.compensations, name="compensations"),
   path('create-compensation/', views.add_compensation, name="create-compensation"),
]