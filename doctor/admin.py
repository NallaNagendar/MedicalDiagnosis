from django.contrib import admin
from .models import DoctorProfile, DoctorHistory

admin.site.register(DoctorProfile)
admin.site.register(DoctorHistory)

