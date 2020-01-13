from django.db import models


class SliderPhoto(models.Model):
    title = models.CharField(max_length=100, help_text='Photo title')
    description = models.TextField(max_length=1000, help_text='Photo description')
    path = models.CharField(max_length=50, help_text='Path to image source (relative, for static)')

    def __str__(self):
        return self.title


class GalleryPhoto(models.Model):
    title = models.CharField(max_length=100, help_text='Photo title')
    description = models.TextField(max_length=1000, help_text='Photo description', null=True)
    path = models.CharField(max_length=50, help_text='Path to the resized image source (in for static)')
    path_original = models.CharField(max_length=50, help_text='Path to the original image source (in static dir)')
    genre = models.CharField(max_length=15, help_text='Image genre (landscape, cityscape, ...)')
    date = models.DateTimeField(null=True)
    location = models.CharField(max_length=80, help_text='Location (coordinates or location name)', null=True)

    def __str__(self):
        return self.title