from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
	#return HttpResponse('<h1>VR Landing</h1>')
	#change to render html page
	return render(request, 'vr/landing.html')

def about(request):
	#return HttpResponse('<h1>VR About</h1>')
	return render(request, 'vr/about.html')