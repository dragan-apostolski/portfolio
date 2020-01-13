from django.shortcuts import render
from .models import SliderPhoto, GalleryPhoto

# Create your views here.


def index(request):
    slider_photos = SliderPhoto.objects.all()
    gallery_landscapes = GalleryPhoto.objects.filter(genre__exact='landscape')
    gallery_cityscape = GalleryPhoto.objects.filter(genre__exact='cityscape')
    context = {'slider_photos': slider_photos,
               'gallery_landscapes': gallery_landscapes,
               'gallery_cityscapes': gallery_cityscape}
    return render(request, 'home/index.html', context=context)
