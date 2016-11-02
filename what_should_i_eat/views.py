from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from os.path import basename

import recipe_book

# Create your views here.

def suggested_recipe(recipes, tags, ingredients):
    return recipes[0]

def index(request):
    recipes = recipe_book.views.get_recipes()
    # TODO: add the logic here
    tags = recipe_book.views.get_tags()
    ingredients = recipe_book.views.get_ingredients()
    recipe = suggested_recipe(recipes, tags, ingredients)
    images = (
        {"url": image.image.url, "name": basename(image.image.url)}
        for image in recipe.image_set.all()
    )
    return render(request, 'what_should_i_eat/index.html', {
        'title': 'suggested recipe',
        'recipe': recipe,
        'tags': tags,
        'ingredients': ingredients,
        'images': images,
    })

def cook_recipe(request, recipe_id):
    recipe = recipe_book.views.get_recipe(recipe_id)

    # TODO: do the logic here
    print("chose this recipe #" + recipe_id)
    return HttpResponseRedirect(reverse('recipe_book:detail', args=(recipe_id)))

def dismiss_recipe(request, recipe_id):
    recipe = recipe_book.views.get_recipe(recipe_id)
    recipe.priority += 1
    recipe.save()
    # stay on the same page and show next best recipe
    return HttpResponseRedirect(reverse('index'))

def recipe_overview(request, recipe_id):
    template = loader.get_template('what_should_i_eat/recipe_overview.html')
    recipes = recipe_book.views.get_recipes()
    tags = recipe_book.views.get_tags()
    ingredients = recipe_book.views.get_ingredients()
    recipe = suggested_recipe(recipes, tags, ingredients)
    images = (
        {"url": image.image.url, "name": basename(image.image.url)}
        for image in recipe.image_set.all()
    )
    context = {
        'recipe': recipe,
        'images': images,
    }
    return JsonResponse({
        'urls': {
            'cook_recipe': reverse('cook_recipe', args=(recipe_id)),
            'dismiss_recipe': reverse('dismiss_recipe', args=(recipe_id)),
        },
        'html': template.render(context, request),
    })
