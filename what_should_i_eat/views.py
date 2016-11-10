import datetime
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from os import path

from recipe_book.models import Recipe, Tag, Ingredient


# HELPERS

def suggest_recipe(recipes, tags, ingredients):
    return (
        recipes
        .filter(Q(tags__in=tags) | Q(ingredients__in=ingredients))
        .order_by("cooked_last", "-priority")
        .first()
    )


# extracts the url and name of all images belonging to a recipe
def prepare_images(recipe):
    if recipe is None:
        return []
    return [
        {
            "url": image.image.url,
            "name": path.basename(image.image.url),
        }
        for image in recipe.images.all()
    ]


# URL-MAPPING FUNCTIONS

def index(request):
    tags = Tag.objects.all()
    ingredients = Ingredient.objects.all()
    recipe = suggest_recipe(
        Recipe.objects.all(),
        tags,
        ingredients
    )
    return render(request, "what_should_i_eat/index.html", {
        "title": "suggested recipe",
        "recipe": recipe,
        "tags": tags,
        "ingredients": ingredients,
        "images": prepare_images(recipe),
    })


def cook_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.priority = 0
    recipe.cooked_last = datetime.date.today()
    recipe.save()
    return HttpResponseRedirect(reverse(
        "recipe_book:detail",
        args=(recipe_id)
    ))


def dismiss_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.priority += 1
    recipe.save()
    # stay on the same page and show next best recipe
    return HttpResponseRedirect(reverse('index'))


@csrf_exempt
def recipe_overview(request, recipe_id):
    template = loader.get_template("what_should_i_eat/recipe_overview.html")
    recipe = suggest_recipe(
        Recipe.objects.all(),
        Tag.objects.filter(
            pk__in=[
                int(tag_id)
                for tag_id in request.POST.getlist("tags[]")
            ]
        ),
        Ingredient.objects.filter(
            pk__in=[
                int(ingredient_id)
                for ingredient_id in request.POST.getlist("ingredients[]")
            ]
        ),
    )
    context = {
        "recipe": (
            recipe
            if recipe is not None
            else {"name": "No recipe found"}
        ),
        "images": prepare_images(recipe),
    }
    return JsonResponse({
        "urls": {
            "cook_recipe": reverse("cook_recipe", args=(recipe_id)),
            "dismiss_recipe": reverse("dismiss_recipe", args=(recipe_id)),
        },
        "html": template.render(context, request),
    })
