from django.shortcuts import render
from .models import SliderPhoto


# Create your views here.

def index(request):
    slider_photos = SliderPhoto.objects.all()
    return render(request, 'home/index.html', context={'slider_photos': slider_photos})
