from django.db import models
from users.models import Student

# Create your models here.


class File(models.Model):
    file = models.FileField()
    tag = models.CharField(max_length=25)
    addedDate = models.DateField()

    def __str__(self):
        return self.tag


class Tag(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.title


class Badge(models.Model):
    picture = models.ImageField()
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=70)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    location = models.CharField(max_length=70)
    text = models.TextField()
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    updateDate = models.DateField()
    helpers = models.ManyToManyField(Student)
    duration = models.DurationField()

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.TextField()
    order = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ContentStep(models.Model):
    TYPE_CHOICES = [
        ( 'ONL', 'En ligne' ),
        ( 'IRL', 'Physique' ),
    ]
    type = models.CharField(max_length=3, choices=TYPE_CHOICES, default='ONL')
    text = models.TextField()
    duration = models.DurationField()
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    tag = models.CharField(max_length=20)
    like = models.IntegerField()
    date = models.DateField()
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    contentStep = models.ForeignKey(ContentStep, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
