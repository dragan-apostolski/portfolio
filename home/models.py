from django.db import models


class SliderPhoto(models.Model):
    title = models.CharField(max_length=100, help_text='Photo title')
    description = models.TextField(max_length=1000, help_text='Photo description')
    path = models.CharField(max_length=50, help_text='Path to image source (relative, for static)')

    def __str__(self):
        return self.title
