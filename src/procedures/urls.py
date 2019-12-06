from django.urls import path
from . import views
from procedures.views import procedure, send_comment, comment_upvote, comment_downvote

urlpatterns = [
    path("<slug:article_slug>", procedure, name="view_procedure"),
    path("<slug:article_slug>/comment", send_comment, name="send_comment"),
    path("<slug:article_slug>/comment/<int:comment_id>/upvote", comment_upvote, name="comment_upvote"),
    path("<slug:article_slug>/comment/<int:comment_id>/downvote", comment_downvote, name="comment_downvote"),
    path('', views.list_procedures)
]
