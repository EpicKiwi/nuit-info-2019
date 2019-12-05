from django.shortcuts import render

# Create your views here.


def index(request):
	return render(request, "index/index.html")


def handler404(request, exception):
	return render(request, 'index/404.html', status=404)