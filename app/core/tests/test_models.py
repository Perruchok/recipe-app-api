from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """Test creating a new user with an email is succesful"""
        email = "diego@home.com"
        password = "diego"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
            Test that email for a new user us normalized
        """

        email = "test@DOMAINNAME"
        user = get_user_model().objects.create_user(email, 'password123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """
            Test craeting user with no email raises error
        """

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "password123")

    def test_create_new_superuser(self):
        """
            Tests creating a new supseruser
        """
        user = get_user_model().objects.create_superuser(
            "test@test.com",
            'passwordtest'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
