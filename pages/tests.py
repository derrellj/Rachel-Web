from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class HomepageTests(TestCase):
    def test_homepage(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_homepage_templates(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home.html")


class UserTest(TestCase):
    def test_create_new_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Derrell", email="derrell@email.com", password="testpassword123456"
        )
        self.assertEqual(user.username, "Derrell")
        self.assertEqual(user.email, "derrell@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username="superadmin", email="superadmin@email.com", password="testpass123"
        )
        self.assertEqual(admin_user.username, "superadmin")
        self.assertEqual(admin_user.email, "superadmin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
