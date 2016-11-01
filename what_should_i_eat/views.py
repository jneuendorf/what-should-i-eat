from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from os.path import basename

import recipe_book

# Create your views here.

def index(request):
    recipes = recipe_book.views.get_recipes()
    # TODO: add the logic here
    recipe = recipes[0]
    tags = recipe_book.views.get_tags()
    ingredients = recipe_book.views.get_ingredients()
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
    return HttpResponseRedirect(reverse('recipe_book:detail', args=(recipe_id,)))

def dismiss_recipe(request, recipe_id):
    recipe = recipe_book.views.get_recipe(recipe_id)
    recipe.priority += 1
    recipe.save()
    # stay on the same page and show next best recipe
    return HttpResponseRedirect(reverse('index'))
