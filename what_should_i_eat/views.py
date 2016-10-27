from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

import recipe_book

# Create your views here.

def index(request):
    recipes = recipe_book.views.recipes()
    # TODO: add the logic here
    recipe = recipes[0]
    return render(request, 'what_should_i_eat/index.html', {
        'title': 'suggested recipe',
        'recipe': recipe,
    })

def cook_next_recipe(request, recipe_id):
    # TODO: do the logic here
    print("chose this recipe #" + recipe_id)
    return HttpResponseRedirect(reverse('index'))

def dismiss_next_recipe(request, recipe_id):
    # TODO: do the logic here
    print("skipping this recipe #" + recipe_id)
    return HttpResponseRedirect(reverse('index'))
