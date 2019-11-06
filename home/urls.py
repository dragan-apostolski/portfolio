from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
]