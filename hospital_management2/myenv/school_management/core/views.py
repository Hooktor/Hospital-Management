from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User, Group
from .models import Patient, Doctor, Appointment, MedicalRecord
from .forms import PatientForm, DoctorForm, AppointmentForm, MedicalRecordForm

@login_required
@permission_required('auth.view_group', raise_exception=True)
def role_list(request):
    roles = Group.objects.all()
    return render(request, 'core/role_list.html', {'roles': roles})

@login_required
@permission_required('auth.view_group', raise_exception=True)
def role_detail(request, group_id):
    role = get_object_or_404(Group, pk=group_id)
    users = role.user_set.all()
    return render(request, 'core/role_detail.html', {'role': role, 'users': users})

@login_required
@permission_required('auth.change_group', raise_exception=True)
def role_assign(request, group_id):
    role = get_object_or_404(Group, pk=group_id)
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        user.groups.add(role)
        return redirect('role_detail', group_id=group_id)
    users = User.objects.exclude(groups__id=group_id)
    return render(request, 'core/role_assign.html', {'role': role, 'users': users})

@login_required
@permission_required('auth.view_user', raise_exception=True)
def dashboard(request):
    stats = {
        'patients': Patient.objects.count(),
        'doctors': Doctor.objects.count(),
        'appointments': Appointment.objects.count(),
        'medical_records': MedicalRecord.objects.count(),
    }
    return render(request, 'core/dashboard.html', {'stats': stats})

@login_required
def index(request):
    is_doctor = request.user.groups.filter(name='Doctor').exists()
    is_patient = request.user.groups.filter(name='Patient').exists()
    return render(request, 'core/index.html', {
        'is_doctor': is_doctor,
        'is_patient': is_patient,
    })

# Patient Views
@login_required
@permission_required('core.add_patient', raise_exception=True)
def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'core/patient_form.html', {'form': form})

@login_required
@permission_required('core.change_patient', raise_exception=True)
def patient_update(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'core/patient_form.html', {'form': form})

@login_required
@permission_required('core.delete_patient', raise_exception=True)
def patient_delete(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'core/patient_confirm_delete.html', {'patient': patient})

@login_required
@permission_required('core.view_patient', raise_exception=True)
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'core/patient_list.html', {'patients': patients})

@login_required
@permission_required('core.view_patient', raise_exception=True)
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    return render(request, 'core/patient_detail.html', {'patient': patient})

# Doctor Views
@login_required
@permission_required('core.add_doctor', raise_exception=True)
def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'core/doctor_form.html', {'form': form})

@login_required
@permission_required('core.change_doctor', raise_exception=True)
def doctor_update(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'core/doctor_form.html', {'form': form})

@login_required
@permission_required('core.delete_doctor', raise_exception=True)
def doctor_delete(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'core/doctor_confirm_delete.html', {'doctor': doctor})

@login_required
@permission_required('core.view_doctor', raise_exception=True)
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'core/doctor_list.html', {'doctors': doctors})

@login_required
@permission_required('core.view_doctor', raise_exception=True)
def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    return render(request, 'core/doctor_detail.html', {'doctor': doctor})

# Appointment Views
@login_required
@permission_required('core.add_appointment', raise_exception=True)
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm()
    return render(request, 'core/appointment_form.html', {'form': form})

@login_required
@permission_required('core.change_appointment', raise_exception=True)
def appointment_update(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointment_list')
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, 'core/appointment_form.html', {'form': form})

@login_required
@permission_required('core.delete_appointment', raise_exception=True)
def appointment_delete(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    if request.method == 'POST':
        appointment.delete()
        return redirect('appointment_list')
    return render(request, 'core/appointment_confirm_delete.html', {'appointment': appointment})

@login_required
@permission_required('core.view_appointment', raise_exception=True)
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'core/appointment_list.html', {'appointments': appointments})

@login_required
@permission_required('core.view_appointment', raise_exception=True)
def appointment_detail(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    return render(request, 'core/appointment_detail.html', {'appointment': appointment})

# MedicalRecord Views
@login_required
@permission_required('core.add_medicalrecord', raise_exception=True)
def medical_record_create(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')
    else:
        form = MedicalRecordForm()
    return render(request, 'core/medical_record_form.html', {'form': form})

@login_required
@permission_required('core.change_medicalrecord', raise_exception=True)
def medical_record_update(request, record_id):
    medical_record = get_object_or_404(MedicalRecord, pk=record_id)
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST, instance=medical_record)
        if form.is_valid():
            form.save()
            return redirect('medical_record_list')
    else:
        form = MedicalRecordForm(instance=medical_record)
    return render(request, 'core/medical_record_form.html', {'form': form})

@login_required
@permission_required('core.delete_medicalrecord', raise_exception=True)
def medical_record_delete(request, record_id):
    medical_record = get_object_or_404(MedicalRecord, pk=record_id)
    if request.method == 'POST':
        medical_record.delete()
        return redirect('medical_record_list')
    return render(request, 'core/medical_record_confirm_delete.html', {'medical_record': medical_record})

@login_required
@permission_required('core.view_medicalrecord', raise_exception=True)
def medical_record_list(request):
    medical_records = MedicalRecord.objects.all()
    return render(request, 'core/medical_record_list.html', {'medical_records': medical_records})

@login_required
@permission_required('core.view_medicalrecord', raise_exception=True)
def medical_record_detail(request, record_id):
    medical_record = get_object_or_404(MedicalRecord, pk=record_id)
    return render(request, 'core/medical_record_detail.html', {'medical_record': medical_record})

# Additional Views
@login_required
@permission_required('auth.change_user', raise_exception=True)
def assign_user_to_group(request, user_id, group_name):
    user = User.objects.get(id=user_id)
    group = Group.objects.get(name=group_name)
    user.groups.add(group)
    user.save()
    return redirect('index')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')