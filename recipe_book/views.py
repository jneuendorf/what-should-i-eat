from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render

from .models import Recipe, Tag, Ingredient
from .forms import AddRecipeForm


# Create your views here.

def index(request):
    recipes = Recipe.objects.order_by('name')
    return render(request, 'recipe_book/index.html', {
        'title': 'recipe book',
        'recipes': recipes,
    })

def add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddRecipeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddRecipeForm()

    return render(request, 'recipe_book/add.html', {'form': form})


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_book/detail.html', {'recipe': recipe})

def tags(request):
    tags = Tag.objects.order_by('name')
    return render(request, 'recipe_book/tags.html', {'tags': tags})


# API to other apps
def get_recipes():
    return Recipe.objects.all()

def get_recipe(recipe_id):
    return get_object_or_404(Recipe, pk=recipe_id)

def get_tags():
    return Tag.objects.all()

def get_ingredients():
    return Ingredient.objects.all()

def get_images_for_recipe(recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return recipe.image_set.all()
