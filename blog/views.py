from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

def photography(request):

	params = {
		'title' : 'Photography Blog',
		'blog_posts' : BlogPost.objects.all().order_by('-date_posted'),
		'meta_desc' : "wb95 blog. Here you will find all the blogs written by wb95."
	}

	return render(request, 'blog/photography.html', params)


def photographyPost(request, post_slug):

	blogPost = BlogPost.objects.get(slug = post_slug)

	params = {
		'post': blogPost,
		'sections': blogPost.section.all(),
		'meta_desc' : "wb95 blog post."
	}

	return render(request, 'blog/photographyDetail.html', params)

