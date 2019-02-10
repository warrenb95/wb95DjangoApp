from django.db import models

class PostImage(models.Model):
	title = models.CharField(max_length=100)
	image_group = models.CharField(max_length=50)
	alt = models.CharField(max_length=100)
	image = models.ImageField(upload_to='media/')
