from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('photography/', views.photography, name='photography'),
    path ('photography/<slug:post_slug>/', views.photographyPost, name='post')
]