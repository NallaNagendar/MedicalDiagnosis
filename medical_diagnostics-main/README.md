# Medical Diagnosing System

Medical Diagnosing System is a web-based healthcare application built using Django, designed to manage patient records and enable doctors to view and analyze patient history. This platform streamlines medical record-keeping and supports better diagnosis through easy access to patient data.

## Tech Stack

- Backend Framework: Django (Python)  
- Frontend: HTML, CSS, JavaScript (Bootstrap optional)  
- Database: SQLite (default), configurable to PostgreSQL/MySQL  
- Authentication: Django’s built-in user auth system  
- IDE: VS Code / PyCharm / any Python-compatible IDE

## Key Features

- User Roles: Patients and Doctors  
- Patient Registration: Secure signup and profile management  
- Medical Records: Patients can enter and update symptoms, conditions, and diagnoses  
- Doctor Access: Doctors can view assigned patient records and medical history  
- Search & Filter: Quickly access patient details using filters (by name, condition, etc.)  
- Security: Role-based access and Django security practices

### Roles
Patient: Register, update profile, submit symptoms

Doctor: View patient list, access medical history, add notes

## Project Structure

medical_diagnosing/
### ├── medical_diagnosing/
## │ ├── settings.py
## │ ├── urls.py
## │ └── ...
### ├── core/
## │ ├── models.py
## │ ├── views.py
## │ ├── urls.py
## │ ├── templates/
## │ │ ├── login.html
## │ │ ├── dashboard.html
## │ │ └── patient_history.html
## ├── db.sqlite3
## ├── manage.py


```bash
git clone https://github.com/yourusername/medical-diagnosing.git
cd medical-diagnosing

## Create Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
pip install -r requirements.txt
## Apply Migrations

python manage.py makemigrations
python manage.py migrate

## Create Superuser (Admin)
python manage.py createsuperuser

## Run the Server
python manage.py runserver

Access the Application
Main App: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/

