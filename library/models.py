from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
