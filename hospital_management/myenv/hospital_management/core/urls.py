from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),

    # URLs for Patient
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/<int:patient_id>/', views.patient_detail, name='patient_detail'),
    path('patients/create/', views.patient_create, name='patient_create'),
    path('patients/<int:patient_id>/edit/', views.patient_update, name='patient_update'),
    path('patients/<int:patient_id>/delete/', views.patient_delete, name='patient_delete'),

    # URLs for Doctor
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
    path('doctors/create/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:doctor_id>/edit/', views.doctor_update, name='doctor_update'),
    path('doctors/<int:doctor_id>/delete/', views.doctor_delete, name='doctor_delete'),

    # URLs for Appointment
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('appointments/<int:appointment_id>/', views.appointment_detail, name='appointment_detail'),
    path('appointments/create/', views.appointment_create, name='appointment_create'),
    path('appointments/<int:appointment_id>/edit/', views.appointment_update, name='appointment_update'),
    path('appointments/<int:appointment_id>/delete/', views.appointment_delete, name='appointment_delete'),

    # URLs for MedicalRecord
    path('medical_records/', views.medical_record_list, name='medical_record_list'),
    path('medical_records/<int:record_id>/', views.medical_record_detail, name='medical_record_detail'),
    path('medical_records/create/', views.medical_record_create, name='medical_record_create'),
    path('medical_records/<int:record_id>/edit/', views.medical_record_update, name='medical_record_update'),
    path('medical_records/<int:record_id>/delete/', views.medical_record_delete, name='medical_record_delete'),

    path('admin/', admin.site.urls),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('roles/', views.role_list, name='role_list'),
    path('roles/<int:group_id>/', views.role_detail, name='role_detail'),
    path('roles/<int:group_id>/assign/', views.role_assign, name='role_assign'),
]