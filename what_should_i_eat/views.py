from django.shortcuts import render

import recipe_book

# Create your views here.

def index(request):
    recipes = recipe_book.views.recipes()
    suggested_recipe = recipes[0]
    return render(request, 'what_should_i_eat/index.html', {'suggested_recipe': suggested_recipe})
