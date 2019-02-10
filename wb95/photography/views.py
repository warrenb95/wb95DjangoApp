from django.shortcuts import render
from django.http import HttpResponse

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
	return HttpResponse("<h1> WORK </h1>")