from django.shortcuts import render, redirect, get_object_or_404
from appointments.models import Appointment
from doctor.models import DoctorProfile
from patient.models import PatientProfile


def book_appointment(request):
    if request.method == "POST":
        doctor_name = request.POST.get("doctor_name")  # Get doctor name from the form
        appointment_date = request.POST.get("appointment_date")

        # Directly assign the doctor to the appointment without validation
        doctor = DoctorProfile.objects.filter(user__username=doctor_name).first()

        # Create the appointment
        Appointment.objects.create(
            patient=request.user.patientprofile,
            doctor=doctor,
            appointment_date=appointment_date,
            status="Pending"
        )
        return redirect('patient:patient_dashboard')  # Ensure this URL is defined correctly

    # Fetch all doctors for the form
    doctors = DoctorProfile.objects.all()
    return render(request, 'patient/book_appointment.html', {'doctors': doctors})




from django.http import HttpResponseRedirect
from patient.models import MedicalRecord

# def upload_records(request):
#     if request.method == "POST":
#         record_file = request.FILES['record_file']
#         insights = request.POST.get("insights")
#         medicines = request.POST.get("medicines")
#         MedicalRecord.objects.create(
#             patient=request.user.patientprofile,
#             record_file=record_file,
#             insights=insights,
#             medicines=medicines
#         )
#         return redirect('patient_dashboard')

#     return render(request, 'patient/upload_records.html')

# views.py for Rating the Doctor
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RateDoctorForm
from doctor.models import DoctorProfile
from appointments.models import Appointment

from django.shortcuts import render, redirect, get_object_or_404
from doctor.models import DoctorProfile
from .forms import RateDoctorForm
from .models import Appointment

def rate_doctor(request, appointment_id):
    # Fetch the appointment using the primary key (id)
    appointment = get_object_or_404(Appointment, id=appointment_id)

    # Ensure the logged-in patient owns the appointment and that the appointment is completed
    if appointment.patient != request.user.patientprofile:
        return redirect('patient:patient_dashboard')  # Redirect if the patient doesn't own the appointment

    if appointment.status != 'Completed':
        # Show a message if the appointment is not completed
        return render(request, 'patient/appointment_not_completed.html')

    if request.method == 'POST':
        form = RateDoctorForm(request.POST)
        if form.is_valid():
            doctor_id = form.cleaned_data['doctor_id']
            rating = form.cleaned_data['rating']

            doctor = get_object_or_404(DoctorProfile, id=doctor_id)

            # Update the doctor's rating based on the patient's input
            doctor.total_reviews += 1
            doctor.ratings = ((doctor.ratings * (doctor.total_reviews - 1)) + rating) / doctor.total_reviews
            doctor.save()

            # Mark the appointment as reviewed
            appointment.status = 'Reviewed'
            appointment.save()

            return redirect('patient:patient_dashboard')
    else:
        form = RateDoctorForm()

    return render(request, 'patient/rate_doctor.html', {'form': form})

from .forms import PatientRegistrationForm
from .models import PatientProfile

# def patient_register(request):
#     if request.method == 'POST':
#         form = PatientRegistrationForm(request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.cleaned_data['password'])
#             user.save()

#             # Create the PatientProfile
#             PatientProfile.objects.create(
#                 user=user,
#                 unique_id=form.cleaned_data['unique_id']
#             )
#             return redirect('login')
#     else:
#         form = PatientRegistrationForm()

#     return render(request, 'patient/register.html', {'form': form})


from .forms import MedicalRecordUploadForm
from .models import MedicalRecord

from django.shortcuts import render, redirect, get_object_or_404
from .forms import MedicalRecordUploadForm
from .models import Appointment

from django.shortcuts import render, redirect, get_object_or_404
from .forms import MedicalRecordUploadForm
from .models import MedicalRecord
from appointments.models import Appointment

def upload_medical_records(request):
    # Fetch the appointment related to the patient, assuming 'Completed' status is a condition
    appointments = Appointment.objects.filter(patient=request.user.patientprofile, status="Completed")

    if appointments.exists():
        # If there are multiple completed appointments, you can choose to select one, e.g., the most recent
        appointment = appointments.order_by('-appointment_date').first()
        # Proceed with your logic for the selected appointment
    else:
        # If no completed appointment is found, render a template to inform the user
        return render(request, 'patient/no_completed_appointments.html')  # Modify or create this template as needed
    # A new template to inform user

    # If the patient doesn't own the appointment, redirect to the dashboard
    if appointment.patient != request.user.patientprofile:
        return redirect('patient:patient_dashboard')

    if request.method == 'POST':
        form = MedicalRecordUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form with the relevant associations
            record = form.save(commit=False)
            record.patient = request.user.patientprofile  # Link to the current patient
            record.doctor = appointment.doctor            # Link to the doctor's profile
            record.appointment = appointment              # Link to the appointment itself
            record.save()  # Save the record
            return redirect('patient:patient_dashboard')  # Redirect to the dashboard
    else:
        form = MedicalRecordUploadForm()

    return render(request, 'patient/upload_records.html', {'form': form})

from django.shortcuts import get_object_or_404
from doctor.models import DoctorProfile
from .forms import RateDoctorForm

# def rate_doctor(request):
#     if request.method == 'POST':
#         form = RateDoctorForm(request.POST)
#         if form.is_valid():
#             doctor_id = form.cleaned_data['doctor_id']
#             rating = form.cleaned_data['rating']

#             doctor = get_object_or_404(DoctorProfile, id=doctor_id)

#             # Update the doctor's ratings
#             doctor.total_reviews += 1
#             doctor.ratings = ((doctor.ratings * (doctor.total_reviews - 1)) + rating) / doctor.total_reviews
#             doctor.save()

#             return redirect('patient:patient_dashboard')
#     else:
#         form = RateDoctorForm()

#     return render(request, 'patient/rate_doctor.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import PatientRegistrationForm


def patient_register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Create Patient Profile
            PatientProfile.objects.create(
                user=user,
                unique_id=form.cleaned_data['unique_id']
            )

            # Automatically log in after registration
            login(request, user)
            return redirect('patient:patient_dashboard')
    else:
        form = PatientRegistrationForm()

    return render(request, 'patient/register.html', {'form': form})


def patient_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('patient:patient_dashboard')  # Redirect to patient's dashboard
        else:
            return render(request, 'patient/login.html', {'error': 'Invalid credentials'})

    return render(request, 'patient/login.html')

from django.shortcuts import render
from appointments.models import Appointment

def patient_dashboard(request):
    # Fetch the appointments associated with the logged-in patient
    appointments = Appointment.objects.filter(patient=request.user.patientprofile)
    
    return render(request, 'patient/patient_dashboard.html', {'appointments': appointments})
