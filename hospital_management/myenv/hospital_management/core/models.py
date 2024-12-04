from django.db import models
from django.contrib.auth.models import User

# In core/models.py

def get_default_user():
    return User.objects.get(id=1)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    patient_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    dob = models.DateField()
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    emergency_contact = models.CharField(max_length=15)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['dob']),
        ]

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, db_index=True)
    specialty = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['specialty']),
        ]

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField()
    reason = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['appointment_date']),
            models.Index(fields=['patient']),
            models.Index(fields=['doctor']),
        ]

class MedicalRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment = models.TextField()
    record_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['record_date']),
            models.Index(fields=['patient']),
            models.Index(fields=['doctor']),
        ]

    def __str__(self):
        return f"{self.patient.user.username} - {self.diagnosis} - {self.record_date}"