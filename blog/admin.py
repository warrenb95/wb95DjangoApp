from django.contrib import admin
from .models import BlogPost, PostSection, Comment

admin.site.register(BlogPost)
admin.site.register(PostSection)
admin.site.register(Comment)