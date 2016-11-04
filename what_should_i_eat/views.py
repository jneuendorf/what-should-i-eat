from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from os import path

from recipe_book.models import Recipe, Tag, Ingredient


# HELPERS

def suggested_recipe(recipes, tags, ingredients):
    # TODO: add the logic here
    # find all recipes that have at least 1 common tag or 1 common ingredient
    print("in suggested_recipe()..............................")
    print("tags:", tags)
    print("ingredients:", ingredients)
    recipes = [
        recipe
        for recipe in recipes.order_by("-cooked_last", "priority")
        if not (
            set(recipe.tags.all()).isdisjoint(tags) and
            set(recipe.ingredients.all()).isdisjoint(ingredients)
        )
    ]
    print("matched recipes:")
    print(recipes)
    if len(recipes) > 0:
        return recipes[0]
    return None


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
    recipe = suggested_recipe(
        Recipe.objects.all(),
        set(tags),
        set(ingredients)
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
    # TODO: do the logic here
    print("chose this recipe #" + recipe_id)
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
    recipe = suggested_recipe(
        Recipe.objects.all(),
        set(Tag.objects.filter(
            pk__in=[
                int(tag_id)
                for tag_id in request.POST.getlist("tags[]")
            ]
        )),
        set(Ingredient.objects.filter(
            pk__in=[
                int(ingredient_id)
                for ingredient_id in request.POST.getlist("ingredients[]")
            ]
        )),
    )
    context = {
        "recipe": recipe,
        "images": prepare_images(recipe),
    }
    return JsonResponse({
        "urls": {
            "cook_recipe": reverse("cook_recipe", args=(recipe_id)),
            "dismiss_recipe": reverse("dismiss_recipe", args=(recipe_id)),
        },
        "html": template.render(context, request),
    })
