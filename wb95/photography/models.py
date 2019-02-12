from django.db import models

class GalleryGroup(models.Model):
	title = models.CharField(max_length=100)
	logo = models.ImageField(upload_to='images/logos')
	desc = models.TextField()

	def __str__(self):
		return self.title


class GalleryImage(models.Model):
	title = models.CharField(max_length=100)
	image_group = models.CharField(max_length=50)
	alt = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/gallery')
	gallery_group = models.ForeignKey(GalleryGroup, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

