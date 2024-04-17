from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('dashboard/', views.dashboard, name="dashboard"),
   path('create-employee/', views.add_employee, name="create-employee"),


   path('department/', views.departments, name="department"),
   path('create-department/', views.add_department, name="create-department"),

   path('compensation/', views.compensations, name="compensations"),
   path('create-compensation/', views.add_compensation, name="create-compensation"),
]