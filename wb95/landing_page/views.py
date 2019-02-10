from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Home view
def home(request):
	return render(request, 'landing_page/home.html')

