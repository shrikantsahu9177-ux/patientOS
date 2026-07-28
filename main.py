import os
from flask import Flask, render_template, request, redirect, url_for, flash
from models.models import db, Patient, Doctor, Appointment
from datetime import date

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, 'ui'),
    static_folder=os.path.join(BASE_DIR, 'assets')
)
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(BASE_DIR, 'database', 'patientos.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'patientos-secret-key-2024'
db.init_app(app)

with app.app_context():
    db.create_all()


# ─── Landing Page ─────────────────────────────────────────────────────────────
@app.route('/')
def home():
    return render_template('index.html')


# ─── Login ────────────────────────────────────────────────────────────────────
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return redirect(url_for('dashboard'))
    return render_template('login/index.html')


# ─── Dashboard ────────────────────────────────────────────────────────────────
@app.route('/dashboard')
def dashboard():
    total_patients = Patient.query.count()
    total_doctors = Doctor.query.count()
    today = date.today().strftime('%Y-%m-%d')
    todays_appointments = Appointment.query.filter_by(date=today).count()
    total_appointments = Appointment.query.count()
    recent_appointments = (
        Appointment.query
        .order_by(Appointment.created_at.desc())
        .limit(5).all()
    )
    return render_template(
        'dashboard/index.html',
        total_patients=total_patients,
        total_doctors=total_doctors,
        todays_appointments=todays_appointments,
        total_appointments=total_appointments,
        recent_appointments=recent_appointments
    )


# ─── Patients ─────────────────────────────────────────────────────────────────
@app.route('/patients')
def patients():
    all_patients = Patient.query.order_by(Patient.created_at.desc()).all()
    return render_template('patient/index.html', patients=all_patients)


@app.route('/patients/add', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        age = request.form['age']
        gender = request.form['gender']
        blood_type = request.form.get('blood_type', '')
        address = request.form.get('address', '')
        patient = Patient(
            name=name, email=email, phone=phone,
            age=int(age), gender=gender, blood_type=blood_type, address=address
        )
        db.session.add(patient)
        db.session.commit()
        flash('Patient registered successfully!', 'success')
        return redirect(url_for('patients'))
    return render_template('patient/add.html')


@app.route('/patients/delete/<int:patient_id>', methods=['POST'])
def delete_patient(patient_id):
    patient = Patient.query.get_or_404(patient_id)
    db.session.delete(patient)
    db.session.commit()
    flash('Patient removed.', 'info')
    return redirect(url_for('patients'))


# ─── Doctors ──────────────────────────────────────────────────────────────────
@app.route('/doctors')
def doctors():
    all_doctors = Doctor.query.order_by(Doctor.created_at.desc()).all()
    return render_template('doctor/index.html', doctors=all_doctors)


@app.route('/doctors/add', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        name = request.form['name']
        specialty = request.form['specialty']
        email = request.form['email']
        phone = request.form['phone']
        department = request.form.get('department', '')
        doctor = Doctor(
            name=name, specialty=specialty,
            email=email, phone=phone, department=department
        )
        db.session.add(doctor)
        db.session.commit()
        flash('Doctor registered successfully!', 'success')
        return redirect(url_for('doctors'))
    return render_template('doctor/add.html')


@app.route('/doctors/delete/<int:doctor_id>', methods=['POST'])
def delete_doctor(doctor_id):
    doctor = Doctor.query.get_or_404(doctor_id)
    db.session.delete(doctor)
    db.session.commit()
    flash('Doctor removed.', 'info')
    return redirect(url_for('doctors'))


# ─── Appointments ─────────────────────────────────────────────────────────────
@app.route('/appointments')
def appointments():
    all_appointments = (
        Appointment.query
        .order_by(Appointment.date.desc(), Appointment.time.desc())
        .all()
    )
    return render_template('appointment/index.html', appointments=all_appointments)


@app.route('/appointments/add', methods=['GET', 'POST'])
def add_appointment():
    patients_list = Patient.query.order_by(Patient.name).all()
    doctors_list = Doctor.query.order_by(Doctor.name).all()
    if request.method == 'POST':
        patient_id = request.form['patient_id']
        doctor_id = request.form['doctor_id']
        appt_date = request.form['date']
        appt_time = request.form['time']
        reason = request.form.get('reason', '')
        appointment = Appointment(
            patient_id=int(patient_id),
            doctor_id=int(doctor_id),
            date=appt_date,
            time=appt_time,
            reason=reason
        )
        db.session.add(appointment)
        db.session.commit()
        flash('Appointment scheduled successfully!', 'success')
        return redirect(url_for('appointments'))
    return render_template('appointment/add.html',
                           patients=patients_list, doctors=doctors_list)


@app.route('/appointments/delete/<int:appt_id>', methods=['POST'])
def delete_appointment(appt_id):
    appt = Appointment.query.get_or_404(appt_id)
    db.session.delete(appt)
    db.session.commit()
    flash('Appointment removed.', 'info')
    return redirect(url_for('appointments'))


# ─── Billing ──────────────────────────────────────────────────────────────────
@app.route('/billing')
def billing():
    return render_template('../pages/billing.html')


# ─── Settings ─────────────────────────────────────────────────────────────────
@app.route('/settings')
def settings():
    return render_template('../pages/settings.html')


# ─── Bed Resource Management ──────────────────────────────────────────────────
@app.route('/bed-management')
def bed_management():
    return render_template('../pages/bed_management.html')


# ─── Emergency Response ───────────────────────────────────────────────────────
@app.route('/emergency')
def emergency():
    return render_template('../pages/emergency.html')


# ─── Security & Audit Logs ────────────────────────────────────────────────────
@app.route('/audit-logs')
def audit_logs():
    return render_template('../pages/audit_logs.html')


if __name__ == '__main__':
    print("Starting PatientOS Enterprise Flask Server on http://localhost:5000")
    app.run(debug=True, port=5000)

