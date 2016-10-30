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
    cooked_last = models.DateField("cooked last on")
    priority = models.PositiveIntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


def get_upload_location(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "recipe_images/{0}/{1}".format(instance.recipe.id, filename)

class Image(models.Model):
    image = models.ImageField(upload_to=get_upload_location)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    #
    # def url(self):
    #     return self.image.url()
