from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Call 07.02.2025
# class Example(models.Model):
#     id = models.IntegerField(primary_key=True)
#     name = models.CharField(max_length=100, unique=True)
#
#
# class Specializations(models.TextChoices):
#     PYTHON = "Python"
#     JAVA = "Java"
#     DATA = "Data"
#
#
# class Mentor(models.Model):
#     name = models.CharField(max_length=70)
#     specialization = models.CharField(max_length=30, choices=Specializations.choices)
#
#
# class Student(models.Model):
#     name = models.CharField(max_length=70)
#     bio = models.TextField()
#     mentor = models.ForeignKey(to=Mentor, on_delete=models.SET_NULL, null=True)

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title