from django.urls import path
from . import views
from procedures.views import procedure, send_comment

urlpatterns = [
    path("<slug:article_slug>", procedure, name="view_procedure"),
    path("<slug:article_slug>/comment", send_comment, name="send_comment"),
    path('', views.list_procedures)
]
