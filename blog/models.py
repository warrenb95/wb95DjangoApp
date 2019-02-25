from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
	title = models.CharField(max_length=100)
	slug = models.CharField(max_length=100)
	image = models.ImageField(upload_to='images/blog/photography', default='')
	description = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title


class PostSection(models.Model):
	post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='section')
	text1 = models.TextField()
	image = models.ImageField(upload_to='images/blog/photography', blank=True, null=True)
	text2 = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.post.title + ' - PK: ' + str(self.pk)


class Comment(models.Model):
	post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comment')
	author = models.CharField(max_length=50)
	comment = models.TextField()

	def __str__(self):
		return self.post.title + ' - Author: ' + self.author