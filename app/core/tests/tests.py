from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating user with email successful """
        email = 'abc@gmail.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Email for new user is normalized """
        email = 'abc@GMAIL.COM'
        user = get_user_model().objects.create_user(email, 'Testpass123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """ Checking user is not created without an email being supplied """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Testpass123')

    def test_create_new_superuser(self):
        """Test creating new superuser """
        user = get_user_model().objects.create_superuser(
            'super@gmail.com',
            'superpass123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)