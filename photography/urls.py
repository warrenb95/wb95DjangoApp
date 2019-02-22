from django.urls import path, include
from . import views

app_name = 'photography'

urlpatterns = [
    path('', views.home, name='photography-home'),
    path('contact/', views.contact, name='photography-contact'),
    path('gallery/', views.gallery, name='photography-gallery'),
    path('blog/', include('blog.urls')),
]