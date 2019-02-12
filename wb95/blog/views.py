from django.shortcuts import render
from django.http import HttpResponse

def photography(request):
	return HttpResponse('<h1> Blog - photography </h1>')
