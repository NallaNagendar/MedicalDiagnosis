from appointments.models import Appointment
from django import forms
from django.contrib.auth.models import User

class AppointmentManagementForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date']
        widgets = {
            'appointment_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
