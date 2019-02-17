from django.contrib import admin
from .models import GalleryImage, GalleryGroup

admin.site.register(GalleryGroup)
admin.site.register(GalleryImage)
