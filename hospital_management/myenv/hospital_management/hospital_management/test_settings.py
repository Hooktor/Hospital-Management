from django.conf import settings
from django.test import TestCase

class TestSettings(TestCase):

    def test_allowed_hosts(self):
        # Check if ALLOWED_HOSTS is as expected for the test environment
        self.assertEqual(settings.ALLOWED_HOSTS, ['testserver'])

    def test_database_settings(self):
        # Check if the test database name is correctly set
        self.assertEqual(settings.DATABASES['default']['NAME'], 'test_school_management_db')

    def test_debug(self):
        # Check if DEBUG is True in the test environment
        self.assertEqual(settings.DEBUG, True)
