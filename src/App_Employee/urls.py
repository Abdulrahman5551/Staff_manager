from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('dashboard/', views.dashboard, name="dashboard"),
   path('create-contact-employee/', views.create_contact, name="create-contact-employee"),
   path('create-employee/', views.create_employee, name="create-employee"),
   path('details-employee/<int:id>/', views.details_employee, name="details-employee"),
   path('update-employee/<int:id>/', views.update_employee, name="update-employee"),

]