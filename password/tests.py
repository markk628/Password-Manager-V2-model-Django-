from django.test import TestCase
from .passwordgen import generate_password

# Create your tests here.
class PasswordTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

class PasswordViewTest(TestCase):
    def test_password(self):
        # password1 = generate_password()
        # password1.save()

        response = self.client.get(f'password/generate/')

        self.assertEqual(response.status_code, 404)