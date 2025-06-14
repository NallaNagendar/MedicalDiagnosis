from django import forms
from django.contrib.auth.models import User
from doctor.models import DoctorProfile

class DoctorRegistrationForm(forms.ModelForm):
    specialization = forms.CharField(max_length=100)
    experience = forms.IntegerField(min_value=0)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

from django import forms
from appointments.models import Appointment

class AppointmentManagementForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['status']
        widgets = {
            'status': forms.Select(choices=[('Accepted', 'Accepted'), ('Rescheduled', 'Rescheduled')]),
        }

