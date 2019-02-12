from django.db import models

class BlogPost(models.Model):
	title = models.CharField(max_length=100)
	post = models.TextField()

	def __str__(self):
		return self.title

	def snippet(self):
		return self.post[:75]


class PostComment(models.Model):
	author = models.CharField(max_length=100)
	comment = models.TextField()
	post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)