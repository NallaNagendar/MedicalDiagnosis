from django.urls import path
from . import views

urlpatterns = [
    path('appointments/', views.view_appointments, name='view_appointments'),  # View all appointments for a doctor or patient
    path('create/', views.create_appointment, name='create_appointment'),  # Create a new appointment
]
