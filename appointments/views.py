from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Appointment
from .forms import AppointmentManagementForm
from doctor.models import DoctorProfile
from patient.models import PatientProfile

# View for doctor to manage appointments (accept/reschedule)
@login_required
def view_appointments(request):
    # If the logged-in user is a doctor, show their appointments
    if hasattr(request.user, 'doctorprofile'):
        doctor = request.user.doctorprofile
        appointments = Appointment.objects.filter(doctor=doctor)
        return render(request, 'appointments/view_appointments.html', {'appointments': appointments, 'is_doctor': True})
    
    # If the logged-in user is a patient, show their appointments
    elif hasattr(request.user, 'patientprofile'):
        patient = request.user.patientprofile
        appointments = Appointment.objects.filter(patient=patient)
        return render(request, 'appointments/view_appointments.html', {'appointments': appointments, 'is_doctor': False})

    return redirect('home')  # Redirect if the user is neither a doctor nor a patient

# Create an appointment view for a patient (Book an appointment)
@login_required
def create_appointment(request):
    if request.method == 'POST':
        doctor_id = request.POST.get('doctor')
        appointment_date = request.POST.get('appointment_date')
        patient = request.user.patientprofile
        doctor = DoctorProfile.objects.get(id=doctor_id)
        
        # Create a new appointment
        appointment = Appointment(
            patient=patient,
            doctor=doctor,
            appointment_date=appointment_date,
            status='Pending'
        )
        appointment.save()
        return redirect('appointments:view_appointments')

    # Display form to select doctor and appointment date
    doctors = DoctorProfile.objects.all()
    return render(request, 'appointments/create_appointment.html', {'doctors': doctors})

# Manage and update appointment status (for doctors)
@login_required
def manage_appointments(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    
    if request.method == 'POST':
        form = AppointmentManagementForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()  # Update the appointment status
            return redirect('appointments:view_appointments')
    else:
        form = AppointmentManagementForm(instance=appointment)

    return render(request, 'appointments/manage_appointment.html', {'form': form, 'appointment': appointment})
