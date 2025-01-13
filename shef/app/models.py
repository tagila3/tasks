from django.db import models

class Shef(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=60)
    chef = models.ForeignKey(Shef, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name