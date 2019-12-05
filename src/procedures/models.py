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
    text = models.CharField(max_length=70)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

