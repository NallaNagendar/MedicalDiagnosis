from django.urls import path
from . import views

app_name = 'patient'

urlpatterns = [
    path('dashboard/',views.patient_dashboard,name='patient_dashboard'),
    path('login/', views.patient_login, name='patient_login'),  # Patient login page
    path('register/', views.patient_register, name='patient_register'),  # Patient registration page
    path('book_appointment/', views.book_appointment, name='book_appointment'),  # Book an appointment
    path('upload-records/', views.upload_medical_records, name='upload_medical_records'),  # Upload medical records
    path('rate-doctor/', views.rate_doctor, name='rate_doctor'),  # Rate a doctor
]
