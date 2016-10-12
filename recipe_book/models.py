from django.db import models
from colorfield.fields import ColorField

# Create your models here.

class Tag(models.Model):
    """docstring for Tag."""

    name = models.CharField(max_length=80)
    color = ColorField(default="2f9de3")
    # recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    """docstring for Recipe."""

    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    description = models.CharField(max_length=2000)
    cooked_last = models.DateTimeField('cooked last on')
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name
