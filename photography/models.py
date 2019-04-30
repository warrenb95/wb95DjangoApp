from django.db import models

class GalleryGroup(models.Model):
	title = models.CharField(max_length=100)
	order = models.IntegerField(null=False)
	logo = models.ImageField(upload_to='images/logos')
	desc = models.TextField()
	video = models.FileField(upload_to='videos/',blank=True, null=True)

	def __str__(self):
		return self.title


class GalleryImage(models.Model):
	gallery_group = models.ForeignKey(GalleryGroup, on_delete=models.CASCADE, related_name='gallery_image')
	image_group = models.CharField(max_length=50)
	alt = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/gallery')

	def __str__(self):
		return self.gallery_group.title

