from django.urls import path
from . import views


urlpatterns = [
    path('' , views.index , name='home'),
    path('cars' , views.cars , name='cars'),
    path('about' , views.about1 , name='about'),
    path('contact' , views.contact , name='contact'),
]