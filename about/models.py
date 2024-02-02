from django.db import models


class AboutPost(models.Model):
    text = models.TextField(blank=False)
    file = models.FileField(upload_to="files/", blank=True)
    image = models.ImageField(upload_to="uploads/", blank=True)

    def sort_content(self):
        if self.file:
            self.text = ""

    def __str__(self):
        return f"{self.text[:50]} - {self.file.url if self.file else ''}"
