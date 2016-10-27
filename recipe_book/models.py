from django.db import models
from colorfield.fields import ColorField

# Create your models here.

class Tag(models.Model):
    """docstring for Tag."""

    name = models.CharField(max_length=80)
    color = ColorField(default="2f9de3")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """docstring for Recipe."""

    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    description = models.TextField()
    cooked_last = models.DateField('cooked last on')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
