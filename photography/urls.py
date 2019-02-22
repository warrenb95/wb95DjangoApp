from django.urls import path, include
from . import views

app_name = 'photography'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('blog/', include('blog.urls')),
]