from django.db import models
from django.utils.text import slugify

from procedures.forms import CommentForm
from users.models import Student


# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=70, unique=True, help_text='--> nom du tag')

	def __str__(self):
		return self.name


class Badge(models.Model):
	picture = models.ImageField()
	name = models.CharField(max_length=70, unique=True, help_text='--> nom du badge')

	def __str__(self):
		return self.name


class Article(models.Model):
	slug = models.CharField(max_length=200, unique=True, blank=True)
	title = models.CharField(max_length=200)
	location = models.CharField(max_length=70)
	text = models.TextField()
	updateDate = models.DateTimeField()
	duration = models.DurationField()
	tag = models.ManyToManyField(Tag)
	helpers = models.ManyToManyField(Student, blank=True)
	author = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="%(app_label)s%(class)s_related",
	                           related_query_name="%(app_label)s%(class)s")

	def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
		self.slug = slugify(self.title)
		return super().save(force_insert, force_update, using, update_fields)

	def __str__(self):
		return self.title


class Step(models.Model):
	title = models.CharField(max_length=200)
	order = models.IntegerField()
	article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="steps")

	def __str__(self):
		return self.title


class ContentStep(models.Model):
	ONLINE = 'ONL'
	IN_REAL_LIFE = 'IRL'
	TYPE_CHOICES = [
		(ONLINE, 'En ligne'),
		(IN_REAL_LIFE, 'Physique'),
	]
	type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='ONL')
	text = models.TextField()
	duration = models.DurationField()
	step = models.ForeignKey(Step, on_delete=models.CASCADE)
	file = models.FileField(upload_to="content-files", blank=True, null=True)

	def get_comment_form(self):
		return CommentForm(data={"step_content_id": self.id})

	def get_best_comments(self):
		return self.comments.order_by("-like")

	def __str__(self):
		return "{} of {}".format(self.type, str(self.step))


class Comment(models.Model):
	text = models.TextField()
	like = models.IntegerField(default=0)
	date = models.DateField(auto_now_add=True)
	file = models.FileField(upload_to="comment-files", blank=True, null=True)
	user = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
	tag = models.ManyToManyField(Tag)
	contentStep = models.ForeignKey(ContentStep, on_delete=models.CASCADE, related_name="comments")

	def __str__(self):
		return self.text
