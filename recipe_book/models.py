from django.db import models
from colorfield.fields import ColorField
import os


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=80)
    color = ColorField(default="#2f9de3")

    def __str__(self):
        return self.name


def ingredient_image_location(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return "ingredient_images/{0}{1}".format(instance.name, file_extension)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=ingredient_image_location, blank=True)
    color = ColorField(default="#e9c871")

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    description = models.TextField()
    cooked_last = models.DateField("cooked last on")
    priority = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag)
    ingredients = models.ManyToManyField(
        Ingredient,
        through="IngredientAmount"
    )

    def __str__(self):
        return self.name


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    recipe = models.ForeignKey(Recipe)
    amount = models.FloatField(default=1)


def recipe_image_location(instance, filename):
    return "recipe_images/{0}/{1}".format(instance.recipe.id, filename)


class Image(models.Model):
    image = models.ImageField(upload_to=recipe_image_location)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="images"
    )
