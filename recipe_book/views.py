import random
import re

# from django.forms import formset_factory
from django.shortcuts import get_object_or_404, render

from .forms import AddRecipeForm, RecipeImageFormSet
from .models import Recipe, Tag, Ingredient, IngredientAmount
from . import utils


# HELPER FUNCTIONS

def rand_color():
    return "#%02X%02X%02X" % (
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )


# VIEW FUNCTIONS

def index(request):
    recipes = Recipe.objects.order_by('name')
    return render(request, 'recipe_book/index.html', {
        'title': 'recipe book',
        'recipes': recipes,
    })


def add(request):
    if request.method == 'POST':
        form = AddRecipeForm(request.POST)
        recipe_image_formset = RecipeImageFormSet(
            request.POST,
            request.FILES,
        )
        if form.is_valid() and recipe_image_formset.is_valid():
            # PARSE TAG NAMES AND INSERT NEW TAGS INTO THE DATABASE
            existing_tags = set(tag.name for tag in Tag.objects.all())
            submitted_tags = (
                set(form.cleaned_data["tags"][0:-1].split(","))
                if len(form.cleaned_data["tags"]) > 0
                else set()
            )
            diff = submitted_tags - existing_tags
            for tag in diff:
                Tag.objects.create(
                    name=tag,
                    color=rand_color()
                )

            # PARSE INGREDIENTS AND INSERT NEW ONES INTO THE DATABASE
            existing_ingredients = set(
                ingredient.name for ingredient in Ingredient.objects.all()
            )
            submitted_ingredients = set(
                re.split("\s*,\s*", form.cleaned_data["ingredients"])
            )

            # map ingredient (incl. amount) -> ingredient name
            submitted_ingredient_names = {
                submitted_ingredient: utils.extract_ingredient_name(
                    submitted_ingredient
                )
                for submitted_ingredient in submitted_ingredients
            }
            diff = (
                set(submitted_ingredient_names.values()) -
                existing_ingredients
            )
            relevant_ingredients = list(Ingredient.objects.filter(
                name__in=submitted_ingredient_names
            ))
            for ingredient in diff:
                relevant_ingredients.append(Ingredient.objects.create(
                    name=ingredient,
                ))

            recipe = Recipe.objects.create(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                cooked_last=form.cleaned_data["cooked_last"],
            )

            recipe.tags = Tag.objects.filter(name__in=submitted_tags)

            for ingredient in submitted_ingredients:
                name = submitted_ingredient_names[ingredient]
                # NOTE: This is difficult because 'name' is a plural
                #       but 'ingredient' might contain the singular of 'name'.
                #       Therefore, if replacing the plural does nothing
                #       (meaning the singular is present in 'ingredient')
                #       then the plural is truncated more and more
                #       until a match happens
                amount = ingredient.replace(name, "").strip()
                truncation = 1
                while amount == ingredient:
                    parts = ingredient.split(name[:-truncation])
                    amount = parts[0].strip()
                    truncation += 1

                IngredientAmount.objects.create(
                    # ingredient=ingredients.filter(name=ingredient).first(),
                    ingredient=Ingredient.objects.get(name=name),
                    # [i for i in relevant_ingredients if i.name == name][0],
                    recipe=recipe,
                    amount=amount,
                )

            recipe.save()

            # cleaned data is used when saving the form
            for recipe_image_form in recipe_image_formset:
                recipe_image_form.instance.recipe = recipe
                # recipe_image_form.save()
            recipe_image_formset.save()

            form = AddRecipeForm()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddRecipeForm()
        recipe_image_formset = RecipeImageFormSet()
        print(recipe_image_formset.initial)
        print([form.initial for form in recipe_image_formset])

    return render(request, 'recipe_book/add.html', {
        'form': form,
        'recipe_image_formset': recipe_image_formset,
        'title': 'new recipe',
    })


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, 'recipe_book/detail.html', {'recipe': recipe})


def tags(request):
    tags = Tag.objects.order_by('name')
    return render(request, 'recipe_book/tags.html', {'tags': tags})
