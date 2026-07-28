# Dynamic Database Integration Plan

To completely remove the hardcoded (dummy) data and allow for real inputs, we need to connect our Flask application to a database and create HTML forms for data entry.

## Proposed Changes

### 1. Database & Models
I will configure an SQLite database inside the `database/` folder. I will use **Flask-SQLAlchemy** to manage the database and create three main models in the `models/` directory:
- **Patient**: ID, Name, Email, Phone, Age, Blood Type, Status
- **Doctor**: ID, Name, Specialty, Email
- **Appointment**: ID, Patient_ID, Doctor_ID, Date, Time, Status

### 2. Registration Forms (Data Input)
I will implement pages to handle new inputs:
- **Patient Registration**: I will copy the exported `add_edit_patient_form` UI into our system at `ui/patient/add.html` and hook it up to a POST route (`/patients/add`).
- **Doctor Registration**: I will create a new doctor registration form at `ui/doctor/add.html` to allow inserting new doctors.
- **New Appointment**: I will create an appointment form at `ui/appointment/add.html` so you can schedule appointments for the registered patients and doctors.

### 3. Dynamic Rendering (Data Output)
I will strip out the hardcoded data from the UI templates and replace them with Jinja2 loops `{% for patient in patients %}`:
- **Dashboard**: Will query the database to show real counts of Total Patients, Today's Appointments, etc.
- **Patients List**: Will display the registered patients from the database.
- **Appointments List**: Will display the scheduled appointments dynamically.
