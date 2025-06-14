from django.urls import path
from . import views

app_name = 'doctor'

urlpatterns = [
     path('update_appointment_status/<int:appointment_id>/', views.update_appointment_status, name='update_appointment_status'),
     path('dashboard/', views.doctor_dashboard, name='doctor_dashboard'),
    path('login/', views.doctor_login, name='doctor_login'),  # Doctor login page
    path('register/', views.doctor_register, name='doctor_register'),  # Doctor registration page
    path('appointments/', views.manage_appointments, name='manage_appointments'),  # Manage appointments (Accept/Reschedule)
    path('history/', views.view_doctor_history, name='doctor_history'),  # Doctor's history (patients treated)
    path('search/', views.search_patient_by_unique_id, name='search_patient'),  # Search patient by unique ID
]


