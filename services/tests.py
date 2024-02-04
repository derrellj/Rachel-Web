from django.test import TestCase
from django.urls import reverse
from .models import Service



class ServicePageViewTest(TestCase):
    def setUp(self):
        # Create some sample Service instances for testing
        Service.objects.create(name="Service 1", service=Service.PEDICURE, price=15.0)
        Service.objects.create(name="Service 2", service=Service.MANICURE, price=25.0)
        Service.objects.create(name="Service 3", service=Service.MAKEUP, price=30.0)

    def test_service_page_view(self):
        url = reverse(
            "services:service"
        )  # Assuming you have a URL pattern named "service"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "services.html")
        self.assertContains(response, "Service 1")
        self.assertContains(response, "Service 2")
        self.assertContains(response, "Service 3")
        self.assertContains(
            response, "15.0"
        )  # Adjust based on your expected price format
        self.assertContains(response, "25.0")
        self.assertContains(response, "30.0")
