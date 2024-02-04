from django.test import TestCase
from django.urls import reverse
from .models import Loc


class LocModelTest(TestCase):
    def setUp(self):
        # Create a sample Loc instance for testing
        Loc.objects.create(text="Test Location", image="path/to/image.jpg")

    def test_model_str_representation(self):
        # Test the __str__ method of the Loc model
        loc_instance = Loc.objects.get(text="Test Location")
        self.assertEqual(str(loc_instance), "Test Location")


class LocPageViewTest(TestCase):
    def setUp(self):
        # Create some sample Loc instances for testing
        Loc.objects.create(text="Location 1", image="path/to/image1.jpg")
        Loc.objects.create(text="Location 2", image="path/to/image2.jpg")

    def test_loc_page_view(self):
        url = reverse("location:loc")  # Assuming you have a URL pattern named "loc"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "location.html")
        self.assertContains(response, "Location 1")
        self.assertContains(response, "Location 2")
