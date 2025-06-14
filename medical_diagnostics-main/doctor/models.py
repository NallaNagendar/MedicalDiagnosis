from django.contrib.auth.models import User
from django.db import models

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()
    ratings = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.user.username} ({self.specialization})"


class DoctorHistory(models.Model):
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE)
    patient = models.ForeignKey('patient.PatientProfile', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Patient {self.patient} treated by {self.doctor}"

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def doctor_dashboard(request):
    # Logic for displaying the doctor's dashboard
    return render(request, 'doctor/dashboard.html')
