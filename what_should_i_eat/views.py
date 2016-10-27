from django.shortcuts import render

import recipe_book

# Create your views here.

def index(request):
    recipes = recipe_book.views.recipes()
    recipe = recipes[0]
    return render(request, 'what_should_i_eat/index.html', {
        'title': 'suggested recipe',
        'recipe': recipe,
    })
