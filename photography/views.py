from django.shortcuts import render
from django.http import HttpResponse
from .models import GalleryGroup

# Create your views here.
def home(request):

	params = {
		"title" : "Home",
		"meta_desc" : "wb95 is the official creative website of photographer, Warren Brown. This is the home page of wb95."
	}

	return render(request, 'photography/home.html', params)


def contact(request):
	params = {
		"title" : "Contact",
		"meta_desc" : "This is the contact page of wb95, please feel free to use this or send an email to wb95.images@gmail.com."
	}
	return render(request, 'photography/contact.html', params)


def gallery(request):

	params = {
		'title': 'Gallery',
		'gallery_groups': GalleryGroup.objects.all(),
		"meta_desc" : "This is the gallery of wb95. Displaying a selction of images taken by wb95."
	}
	return render(request, 'photography/gallery.html', params)