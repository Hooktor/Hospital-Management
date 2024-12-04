from django.contrib import admin
from .models import Patient, Doctor, Appointment, MedicalRecord
from django.contrib.auth.admin import UserAdmin



# Remove this line if it exists
# admin.site.register(User)

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)