from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
	return redirect(reverse("list_procedures"))


def handler404(request, exception):
	return render(request, 'index/404.html', status=404)