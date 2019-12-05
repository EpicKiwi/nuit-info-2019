from django.db import models


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


class File(models.Model):
    text = models.TextField(help_text='Description du fichier')
    file = models.FileField()

    def __str__(self):
        return self.file.attname


class Student(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    location = models.CharField(max_length=128)
    creationDate = models.DateTimeField()
    badge = models.ManyToManyField(Badge, on_delete=models.CASCADE)

    def __str__(self):
        return self.surname


class Article(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=70)
    text = models.TextField()
    updateDate = models.DateTimeField()
    duration = models.DurationField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    helpers = models.ManyToManyField(Student, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Step(models.Model):
    title = models.CharField(max_length=200)
    order = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

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
    file = models.ForeignKey(File, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Comment(models.Model):
    text = models.TextField()
    like = models.IntegerField()
    date = models.DateField()
    file = models.ManyToOneRel(File, on_delete=models.CASCADE)
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, on_delete=models.CASCADE)
    contentStep = models.ForeignKey(ContentStep, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
