from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import BlogPost, Comment
from .forms import CommentForm

def photography(request):

	params = {
		'title' : 'Photography Blog',
		'blog_posts' : BlogPost.objects.all().order_by('-date_posted'),
		'meta_desc' : "wb95 blog. Here you will find all the blogs written by wb95."
	}

	return render(request, 'blog/photography.html', params)


def photographyPost(request, post_slug):

	blogPost = BlogPost.objects.get(slug = post_slug)

	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			com = form.save(commit=False)
			com.post_id = blogPost.pk

			comment_qs = None

			reply_id = request.POST.get('comment_id')

			if reply_id:
				comment_qs = blogPost.comment.get(id=reply_id)

			com.reply = comment_qs
			com.save()

			return redirect('blog:post', blogPost.slug)

	else:
		form = CommentForm()

	params = {
		'post': blogPost,
		'title': blogPost.title,
		'form': form,
		'meta_desc' : "wb95 blog post."
	}

	return render(request, 'blog/photographyDetail.html', params)

