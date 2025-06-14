from django import forms
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from patient.models import PatientProfile

class PatientRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    unique_id = forms.CharField(max_length=100)  # Assuming unique_id is a CharField

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'unique_id']

    def clean_unique_id(self):
        unique_id = self.cleaned_data.get('unique_id')
        if PatientProfile.objects.filter(unique_id=unique_id).exists():
            raise forms.ValidationError("This unique ID is already in use. Please enter a different one.")
        return unique_id

from django import forms
from patient.models import MedicalRecord

class MedicalRecordUploadForm(forms.ModelForm):
    class Meta:
        model = MedicalRecord
        fields = ['record_file', 'description']  

class RateDoctorForm(forms.Form):
    doctor_id = forms.IntegerField(widget=forms.HiddenInput())  # To keep doctor ID hidden
    rating = forms.FloatField(min_value=0.0, max_value=5.0, widget=forms.NumberInput(attrs={'step': 0.5, 'max': 5.0, 'min': 0.0}))  # Rating between 0.0 and 5.0

