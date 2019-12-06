from django.shortcuts import render
from django.http import HttpResponse


def list_procedures(request):
    return render(request, 'procedures/list_procedures.html')
