from django.contrib import admin
from procedures.models import Article, Step, Tag, ContentStep, Badge


# Register your models here.


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	pass


@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
	pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	pass


@admin.register(ContentStep)
class ContentStepAdmin(admin.ModelAdmin):
	pass


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
	pass