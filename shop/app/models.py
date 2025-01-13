from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=50)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Position(models.Model):
    position = models.CharField(max_length=30)

    def __str__(self):
        return self.position