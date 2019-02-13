from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost, PostSection, PostComment

def photography(request):

	params = {
		'title' : 'Photography Blog',
		'blog_posts' : BlogPost.objects.all()
	}

	return render(request, 'blog/photography.html', params)


def photographyPost(request, post_slug):

	blogPost = BlogPost.objects.get(slug = post_slug)

	params = {
		'title': blogPost.title,
		'sections': PostSection.objects.filter(post = blogPost.id)
	}

	return render(request, 'blog/photographyDetail.html', params)

