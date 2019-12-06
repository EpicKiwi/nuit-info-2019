from django.urls import path
from . import views
from procedures.views import procedures

urlpatterns = [
    path("<slug:article_slug>", procedures),
    path('', views.list_procedures)
]
