from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=20)
    publication_date = models.DateField()
    author = models.ManyToManyField(Author)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
