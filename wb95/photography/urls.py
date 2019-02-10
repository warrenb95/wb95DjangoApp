from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='photography-home'),
    path('contact/', views.contact, name='photography-contact'),
    path('gallery/', views.gallery, name='photography-gallery'),
]