from django.test import TestCase
from django.urls import reverse
from django.contrib.admin.sites import AdminSite
from .admin import AboutPostAdmin
from .models import AboutPost





class AboutPostAdminTest(TestCase):
    def setUp(self):
        # Create a sample AboutPost for testing
        self.about_post = AboutPost.objects.create(
            text="Sample About Text", image="path/to/sample/image.jpg"
        )

        # Set up the admin site
        self.site = AdminSite()
        self.model_admin = AboutPostAdmin(AboutPost, self.site)

    def test_admin_display_text(self):
        displayed_text = self.model_admin.display_text(self.about_post)
        self.assertEqual(displayed_text, "Sample About Text")


class AboutPostModelTest(TestCase):
    def setUp(self):
        # Create a sample AboutPost for testing
        self.about_post = AboutPost.objects.create(
            text="Sample About Text", image="path/to/sample/image.jpg"
        )

    def test_model_str_representation(self):
        self.assertEqual(str(self.about_post), "Sample About Text")


class AboutPageViewTest(TestCase):
    def setUp(self):
        # Create a sample AboutPost for testing
        self.about_post = AboutPost.objects.create(
            text="Sample About Text", image="path/to/sample/image.jpg"
        )

    def test_about_page_view(self):
        url = reverse("about:about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "about.html")
        self.assertContains(
            response, "Sample About Text"
        )  # Check if the text is present in the rendered HTML
        # Add more specific assertions based on your view's behavior

    # Add more tests as needed
