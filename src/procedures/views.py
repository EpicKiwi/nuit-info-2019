from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from procedures.forms import CommentForm
from procedures.models import Article, Step, Comment, ContentStep


def list_procedures(request):

    articles = Article.objects.all()

    return render(request, 'procedures/list_procedures.html', locals())


def procedure(request, article_slug):

    article = get_object_or_404(Article, slug=article_slug)
    steps = article.steps.all().order_by("order")

    return render(request, "procedures.html", locals())

def send_comment(request, article_slug):

    if not request.method == "POST":
        return redirect(reverse("view_procedure", args=[article_slug]))

    filled_form = CommentForm(request.POST)

    comment = None

    if filled_form.is_valid():
        step_content = get_object_or_404(ContentStep, id=filled_form.cleaned_data["step_content_id"])
        comment = Comment.objects.create(contentStep=step_content, text=filled_form.cleaned_data["comment"])

    return redirect(
        reverse("view_procedure", args=[article_slug]) +
        "?highlight_comment={}".format(comment.id if comment is not None else None))

