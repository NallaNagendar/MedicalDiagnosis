from django.db import models
from django.db import models
import uuid

class Appointment(models.Model):
    patient = models.ForeignKey('patient.PatientProfile', on_delete=models.CASCADE)
    doctor = models.ForeignKey('doctor.DoctorProfile', on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rescheduled', 'Rescheduled')],
        default='Pending'
    )

    def __str__(self):
        return f"Appointment with {self.doctor} on {self.appointment_date}"
