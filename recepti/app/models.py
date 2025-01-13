from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=40)
    instructions = models.CharField(max_length=50)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.TextField(max_length=500)

    def __str__(self):
        return self.name