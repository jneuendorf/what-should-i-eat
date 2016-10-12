from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Recipe, Tag


# Create your views here.

def index(request):
    recipes = Recipe.objects.order_by('name')
    return render(request, 'recipe_book/index.html', {'recipes': recipes})

def add(request):
    return HttpResponse("You want to add a recipe?")

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_book/detail.html', {'recipe': recipe})

def tags(request):
    tags = Tag.objects.order_by('name')
    return render(request, 'recipe_book/tags.html', {'tags': tags})
