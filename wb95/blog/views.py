from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost, PostComment

def photography(request):

	params = {
		"title" : "Photography Blog",
		"blog_posts" : BlogPost.objects.all()
	}

	return render(request, 'blog/photographyBlog.html', params)
