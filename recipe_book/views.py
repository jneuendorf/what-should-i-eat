import random
import re

from django.shortcuts import get_object_or_404, render

from .forms import AddRecipeForm
from .models import Recipe, Tag, Ingredient
from . import utils


# Create your views here.

def index(request):
    recipes = Recipe.objects.order_by('name')
    return render(request, 'recipe_book/index.html', {
        'title': 'recipe book',
        'recipes': recipes,
    })


def add(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        if form.is_valid():
            # PARSE TAG NAMES AND INSERT NEW TAGS INTO THE DATABASE
            existing_tags = set(tag.name for tag in Tag.objects.all())
            submitted_tags = set(form.cleaned_data["tags"][0:-1].split(","))
            diff = submitted_tags - existing_tags
            for tag in diff:
                color = "#%02X%02X%02X" % (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
                Tag.objects.create(
                    name=tag,
                    color=color
                )

            # PARSE INGREDIENTS AND INSERT NEW ONES INTO THE DATABASE
            existing_ingredients = set(
                ingredient.name for ingredient in Ingredient.objects.all()
            )
            submitted_ingredients = set(
                re.split("\s*,\s*", form.cleaned_data["ingredients"])
            )

            submitted_ingredient_names = set([
                utils.extract_ingredient_name(submitted_ingredient)
                for submitted_ingredient in submitted_ingredients
            ])
            submitted_ingredient_amounts = set()
            print(submitted_ingredient_names)
            diff = submitted_ingredient_names - existing_ingredients
            for ingredient in diff:
                Ingredient.objects.create(
                    name=ingredient,
                )

            # recipe = Recipe.objects.create(
            #     name=recipe1_name,
            #     description=recipe1_desc,
            #     cooked_last=datetime.date.today(),
            # )

            # recipe.tags = Tag.objects.filter(name__in=submitted_tags)

            # IngredientAmount.objects.create(
            #     ingredient=ingredient1,
            #     recipe=recipe,
            #     amount=ingredient_amount1_amount,
            # )
            # recipe.save()

            # form cleaned data: {
            #     'ingredients_choices': '',
            #     'name': 'test recipe',
            #     'description': 'adsf',
            #     'ingredients': '50 g Butter',
            #     'cooked_last': datetime.date(2016, 11, 16),
            #     'images': None,
            #     'tags': 'Italian,'
            # }

            # form = AddRecipeForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddRecipeForm()

    return render(request, 'recipe_book/add.html', {
        'form': form,
        'title': 'new recipe',
    })


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_book/detail.html', {'recipe': recipe})


def tags(request):
    tags = Tag.objects.order_by('name')
    return render(request, 'recipe_book/tags.html', {'tags': tags})
