from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home view
def home(request):
	return HttpResponse("<h1>Home</h1>")
