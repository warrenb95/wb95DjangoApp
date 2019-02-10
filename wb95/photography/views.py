from django.shortcuts import render
from django.http import HttpResponse
from .models import PostImage

# Create your views here.
def home(request):

	params = {
		"title" : "Home"
	}

	return render(request, 'photography/home.html', params)


def contact(request):
	params = {
		"title" : "Contact"
	}
	return render(request, 'photography/contact.html', params)


def gallery(request):
	params = {
		'title': 'Gallery',
		'images': PostImage.objects.all()
	}
	return render(request, 'photography/gallery.html', params)