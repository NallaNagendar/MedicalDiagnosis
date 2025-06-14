from django.contrib.auth.models import User
from django.db import models
from django.db import models
from doctor.models import DoctorProfile
from appointments.models import Appointment

class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.user.username} (ID: {self.unique_id})"

class MedicalRecord(models.Model):
    patient = models.ForeignKey(PatientProfile, on_delete=models.CASCADE)
    doctor = models.ForeignKey(DoctorProfile, on_delete=models.CASCADE,null=True)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, null=True, blank=True)
    record_file = models.FileField(upload_to='medical_records/')
    description = models.TextField()

    def __str__(self):
        return f"Record for {self.patient} with Dr. {self.doctor}"

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def patient_dashboard(request):
    # Logic for displaying the patient's dashboard
    return render(request, 'patient/dashboard.html')
