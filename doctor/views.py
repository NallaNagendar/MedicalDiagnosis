from django.shortcuts import render, redirect, get_object_or_404
from appointments.models import Appointment
from doctor.models import DoctorHistory
from patient.models import PatientProfile, MedicalRecord
from django.contrib.auth.decorators import login_required


def home1(request):
    return render(request, 'doctor/home.html')  

from django.shortcuts import render, redirect, get_object_or_404
from appointments.models import Appointment

from django.shortcuts import render, get_object_or_404, redirect
from appointments.models import Appointment

from django.shortcuts import render
from appointments.models import Appointment

def manage_appointments(request):
    # Fetch all appointments for the logged-in doctor
    appointments = Appointment.objects.filter(doctor__user=request.user)
    
    # Print all appointments for debugging
    for appointment in appointments:
        print(f"Appointment with Patient: {appointment.patient.user.username}, Status: {appointment.status}, Date: {appointment.appointment_date}")

    return render(request, 'doctor/manage_appointments.html', {'appointments': appointments})



@login_required
def view_doctor_history(request):
    doctor_profile = request.user.doctorprofile
    history = doctor_profile.doctorhistory_set.all()
    return render(request, 'doctor/history.html', {'history': history})

# Search patient by unique ID
@login_required
@login_required
def search_patient_by_unique_id(request):
    if request.method == 'POST':
        unique_id = request.POST.get('unique_id')
        try:
            patient = PatientProfile.objects.get(unique_id=unique_id)
            medical_records = patient.medicalrecord_set.all()

            # Adding appointment dates to each medical record
            for record in medical_records:
                record.appointment_date = record.appointment.appointment_date if record.appointment else None

            return render(request, 'doctor/patient_history.html', {'patient': patient, 'medical_records': medical_records})
        except PatientProfile.DoesNotExist:
            # Handle patient not found
            pass
    return render(request, 'doctor/search_patient.html')


from django.shortcuts import render, redirect
from .forms import DoctorRegistrationForm
from .models import DoctorProfile

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import DoctorRegistrationForm

def doctor_register(request):
    if request.method == 'POST':
        form = DoctorRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create Doctor Profile
            DoctorProfile.objects.create(
                user=user,
                specialization=form.cleaned_data['specialization'],
                experience=form.cleaned_data['experience']
            )

            # Automatically log in after registration
            login(request, user)
            return redirect('doctor:doctor_dashboard')
    else:
        form = DoctorRegistrationForm()

    return render(request, 'doctor/register.html', {'form': form})

def doctor_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('doctor:doctor_dashboard')  # Redirect to doctor's dashboard
        else:
            return render(request, 'doctor/login.html', {'error': 'Invalid credentials'})

    return render(request, 'doctor/login.html')

def doctor_dashboard(request):
    # Your view logic for the doctor dashboard
    return render(request, 'doctor/doctor_dashboard.html')

from django.shortcuts import render, get_object_or_404, redirect
from appointments.models import Appointment
from django.contrib.auth.decorators import login_required

@login_required
def update_appointment_status(request, appointment_id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=appointment_id)
        new_status = request.POST.get('status')
        if new_status in ['Pending', 'Accepted', 'Completed']:
            appointment.status = new_status
            appointment.save()
            return redirect('doctor:manage_appointments')  # Replace with the name of the URL pattern for the appointments page
    return redirect('doctor:manage_appointments')  # Redirect back if the request is not POST or status is invalid
