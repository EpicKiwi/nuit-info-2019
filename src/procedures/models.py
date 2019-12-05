from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=70)
    surname = models.CharField(max_length=70)
    location = models.CharField(max_length=70)

    def __str__(self):
        return self.name + ' ' + self.surname


class Article(models.Model):
    title = models.CharField(max_length=70)
    tag = models.CharField(max_length=70)
    location = models.CharField(max_length=70)
    text = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    score = models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    score = models.IntegerField()
    date = models.DateField()
    location = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)

    def __str__(self):
        return self.text

