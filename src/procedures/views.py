from django.shortcuts import render
from django.http import HttpResponse


def list_procedures(request):
    return render(request, 'procedures/list_procedures.html')


def procedures(request, article_slug):
    return render(request, "procedures.html", {'article': article_slug})

