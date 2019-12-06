from django.shortcuts import render
from django.http import HttpResponse
from procedures.models import Article


def list_procedures(request):
    allProcedures = Article.objects.all()
    return render(request, 'procedures/list_procedures.html', {"procedures": allProcedures})
