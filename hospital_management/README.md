# Hospital Management System

## Overview

The Hospital Management System is a web application built with Django that allows administrators to manage patients, doctors, appointments, and medical records. The system provides functionalities for CRUD operations, detailed reports, and role-based access control.

## Features

### Patient Management

- Enrollment (add/update/delete patients)
- Maintain personal details like name, date of birth, address, and contact information

### Doctor Management

- Manage doctor information (name, specialty, contact details)

### Appointment Management

- Schedule and manage appointments between patients and doctors

### Medical Record Management

- Record and update medical records for patients
- Generate medical record reports

### Administration Features

- Define roles (admin, doctor, patient) with specific privileges
- Backup and restore database functionality

## Installation

### Prerequisites

- Python 3.12
- Django 5.1.3
- MySQL

### Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure the database:
   Edit `hospital_management/settings.py` to configure the database settings.

6. Create the MySQL database:

   ```sql
   CREATE DATABASE hospitaldb;
   ```

7. Run migrations:

   ```bash
   python manage.py migrate
   ```

8. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

9. Run the development server:

   ```bash
   python manage.py runserver
   ```

10. Access the application:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

### Role-Based Access Control

#### Create Groups and Assign Permissions:

Use the Django shell to create groups and assign permissions.

#### Assign Users to Groups:

Use the Django shell to assign users to groups.

### Backup and Restore

#### Backup the database:

```bash
mysqldump -u username -p hospital_management > backup.sql
```

#### Restore the database:

```bash
mysql -u username -p hospital_management < backup.sql
```

### Detailed Reports

#### Medical Record Report:

Access the medical record report at `http://127.0.0.1:8000/medical-records/report/`.

#### Appointment Report:

Access the appointment report at `http://127.0.0.1:8000/appointments/report/`.

## Database Schema

### Entities

- Patients (PatientID, Name, DOB, Address, ContactNumber, EmergencyContact)
- Doctors (DoctorID, Name, Specialty, ContactNumber)
- Appointments (AppointmentID, PatientID, DoctorID, AppointmentDate, Reason)
- MedicalRecords (RecordID, PatientID, DoctorID, Diagnosis, Treatment, RecordDate)
- Users (UserID, Username, Password, Role)

### Relationships

- Patients → Appointments: One-to-Many (a patient can have multiple appointments).
- Doctors → Appointments: One-to-Many (a doctor can have multiple appointments).
- Patients → MedicalRecords: One-to-Many (a patient can have multiple medical records).
- Doctors → MedicalRecords: One-to-Many (a doctor can have multiple medical records).

### Normalized Database Schema (3NF)

- 1NF: Each column contains atomic data, and each table has a unique identifier (primary key).
- 2NF: All non-primary key attributes are functionally dependent on the entire primary key.
- 3NF: Transitive dependencies are eliminated.

## Technical Choices

### Indexes

- B-Tree Indexes: Used for range queries (e.g., finding patients born in a specific year).
- Hash Indexes: Suitable for exact lookups (e.g., fetching a patient by PatientID).

### Partitioning Strategy

- By Department: Separate tables/partitions for each department to optimize performance when querying or updating data for a specific department.
- By Year: If the system scales to include historical data, partition by year to enhance scalability.

### Security

#### Creation of Users for Each Role:

- Admin, Doctor, Patient

#### Assignment of Privileges:

- Admin: Full access
- Doctor: Access to patient, appointment, and medical record management
- Patient: Access to their own records

#### Protection Against SQL Injections:

- Use Django ORM for database queries

### Backup Plan

#### Strategy (Full and Incremental):

- Full backups weekly
- Incremental backups daily

#### Restoration Procedures:

- Documented steps for restoring from backups

#### Recovery Tests:

- Regularly test backup and restoration procedures to ensure data integrity

This README.md should provide a comprehensive guide for setting up and using your hospital management system project.
