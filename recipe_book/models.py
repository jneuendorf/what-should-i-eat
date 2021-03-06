from django.db import models
from colorfield.fields import ColorField
import os


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=80, unique=True)
    color = ColorField(default="#2f9de3")

    def __str__(self):
        return self.name


def ingredient_image_location(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return "ingredient_images/{0}{1}".format(instance.name, file_extension)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to=ingredient_image_location, blank=True)
    color = ColorField(default="#e9c871", blank=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=200)
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

    def ingredient_list(self):
        return ", ".join(
            "{0} {1}".format(
                ingredient_amount.amount,
                ingredient_amount.ingredient.name
            )
            for ingredient_amount in self.ingredient_amounts.all()
        )


class IngredientAmount(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE,)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="ingredient_amounts"
    )
    amount = models.CharField(max_length=50, default="")

    def __str__(self):
        return "{0} of {1} for {2}".format(
            self.amount,
            self.ingredient,
            self.recipe
        )


def recipe_image_location(instance, filename):
    if type(instance) is Image:
        id = instance.recipe.id
    elif type(instance) is Recipe:
        id = instance.id
    else:
        raise ValueError("recipe_image_location() expects an image or recipe model.")
    return "recipe_images/{0}/{1}".format(id, filename)


class Image(models.Model):

    # @staticmethod
    # def recipe_image_location(instance, filename):
    #     return "recipe_images/{0}/{1}".format(instance.recipe.id, filename)

    image = models.ImageField(upload_to=recipe_image_location)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name="images"
    )
