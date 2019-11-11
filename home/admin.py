from django.contrib import admin
from .models import SliderPhoto


# Register your models here.


class SliderPhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'path']


admin.site.register(SliderPhoto, SliderPhotoAdmin)
