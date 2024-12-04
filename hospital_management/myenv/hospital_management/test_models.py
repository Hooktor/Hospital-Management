import django
from django.conf import settings
from django.core.management import call_command
from django.test import TestCase
from core.models import Student, Teacher, Class, Subject, Grade, Attendance
from django.contrib.auth.models import User

# Ensure settings are only configured once
if not settings.configured:
    settings.configure(
        INSTALLED_APPS=[
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'core',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'school_management_db',  # Replace with your database name
                'USER': 'root',       # Replace with your MySQL user
                'PASSWORD': 'root',  # Replace with your MySQL password
                'HOST': 'localhost',             # Set to your database host
                'PORT': '3306',                  # Set to your database port
            }
        },
        USE_TZ=True,
        TIME_ZONE='UTC',
        DEBUG=True,  # Ensure DEBUG is set to True for tests
    )

# Initialize Django
django.setup()

# Test if Django models are working correctly
class TestModel(TestCase):

    def setUp(self):
        # Create a user for Student
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create Teacher
        self.teacher = Teacher.objects.create(
            name='Test Teacher',
            subject='Mathematics',
            contact_number='1234567890'
        )

        # Create Class
        self.class_instance = Class.objects.create(
            name='Class 1',
            teacher_id=self.teacher
        )

        # Create Subject
        self.subject = Subject.objects.create(
            name='Algebra',
            teacher_id=self.teacher
        )

        # Create Student
        self.student = Student.objects.create(
            user=self.user,
            name='Jane Smith',
            dob='2000-01-01',
            address='123 Main St',
            contact_number='0987654321',
            class_id=self.class_instance
        )

        # Create Grade
        self.grade = Grade.objects.create(
            student_id=self.student,
            subject_id=self.subject,
            marks=95
        )

        # Create Attendance
        self.attendance = Attendance.objects.create(
            student_id=self.student
        )

    def test_student_creation(self):
        self.assertEqual(self.student.name, 'Jane Smith')

    def test_teacher_creation(self):
        self.assertEqual(self.teacher.name, 'Test Teacher')

    def test_class_creation(self):
        self.assertEqual(self.class_instance.name, 'Class 1')

    def test_subject_creation(self):
        self.assertEqual(self.subject.name, 'Algebra')

    def test_grade_creation(self):
        self.assertEqual(self.grade.marks, 95)

    def test_attendance_creation(self):
        self.assertEqual(self.attendance.student_id, self.student)

    def test_update_student(self):
        # Test updating a student
        self.student.name = 'Updated Student'
        self.student.save()
        updated_student = Student.objects.get(pk=self.student.student_id)
        self.assertEqual(updated_student.name, 'Updated Student')

    def test_delete_student(self):
        # Test deleting a student
        student_id = self.student.student_id
        self.student.delete()
        with self.assertRaises(Student.DoesNotExist):
            Student.objects.get(pk=student_id)

    def test_querying(self):
        # Test if querying works correctly
        student = Student.objects.get(pk=self.student.student_id)
        self.assertEqual(student.class_id.name, 'Class 1')

    def test_debug(self):
        self.assertEqual(settings.DEBUG, True)

# If you want to run the tests programmatically, use call_command
if __name__ == '__main__':
    # Run the tests
    call_command('test', 'core')  # Replace 'core' with your app name