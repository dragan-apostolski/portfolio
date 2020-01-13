from django.contrib import admin
from .models import SliderPhoto, GalleryPhoto


# Register your models here.


class SliderPhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'path']


class GalleryPhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'date', 'location', 'path', 'path_original', 'genre']


admin.site.register(SliderPhoto, SliderPhotoAdmin)
admin.site.register(GalleryPhoto, GalleryPhotoAdmin)
