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
            submitted_tags = (
                set(form.cleaned_data["tags"][0:-1].split(","))
                if len(form.cleaned_data["tags"]) > 0
                else set()
            )
            diff = submitted_tags - existing_tags
            print(existing_tags, submitted_tags)
            print("diff", diff)
            for tag in diff:
                color = "#%02X%02X%02X" % (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255)
                )
                # Tag.objects.create(
                #     name=tag,
                #     color=color
                # )
                print(
                    "would create a tag with name '{0}' and color {1}"
                    .format(tag, color)
                )

            # PARSE INGREDIENTS AND INSERT NEW ONES INTO THE DATABASE
            existing_ingredients = set(
                ingredient.name for ingredient in Ingredient.objects.all()
            )
            submitted_ingredients = set(
                re.split("\s*,\s*", form.cleaned_data["ingredients"])
            )

            # submitted_ingredient_names = set([
            #     utils.extract_ingredient_name(submitted_ingredient)
            #     for submitted_ingredient in submitted_ingredients
            # ])
            # map ingredient (incl. amount) -> ingredient name
            submitted_ingredient_names = {
                submitted_ingredient: utils.extract_ingredient_name(
                    submitted_ingredient
                )
                for submitted_ingredient in submitted_ingredients
            }
            submitted_ingredient_amounts = set()
            # print(submitted_ingredient_names)
            diff = (
                set(submitted_ingredient_names.values()) -
                existing_ingredients
            )
            relevant_ingredients = list(Ingredient.objects.filter(
                name__in=submitted_ingredient_names
            ))
            for ingredient in diff:
                # Ingredient.objects.create(
                #     name=ingredient,
                # )
                # relevant_ingredients.append(Ingredient.objects.create(
                #     name=ingredient,
                # ))
                relevant_ingredients.append(Ingredient(name=ingredient))
                print(
                    "would create ingredient with name '{0}'"
                    .format(ingredient)
                )

            # recipe = Recipe.objects.create(
            #     name=form.cleaned_data["name"],
            #     description=form.cleaned_data["description"],
            #     cooked_last=form.cleaned_data["cooked_last"],
            # )
            recipe = Recipe(
                name=form.cleaned_data["name"],
                description=form.cleaned_data["description"],
                cooked_last=form.cleaned_data["cooked_last"],
            )
            print(
                "would create recipe with name '{0}', description '{1}' "
                "and cooked_last '{2}'"
                .format(
                    form.cleaned_data["name"],
                    form.cleaned_data["description"],
                    form.cleaned_data["cooked_last"],
                )
            )

            # recipe.tags = Tag.objects.filter(name__in=submitted_tags)
            print(
                "would set recipe.tags to {0}"
                .format(Tag.objects.filter(name__in=submitted_tags))
            )

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

                # IngredientAmount.objects.create(
                #     ingredient=ingredients.filter(name=ingredient).first(),
                #     recipe=recipe,
                #     amount=amount,
                # )
                print(
                    "would create IngredientAmount with ingredient '{0}', "
                    "recipe '{1}' and amount '{2}'"
                    .format(
                        # relevant_ingredients.get(name=ingredient),
                        [i for i in relevant_ingredients if i.name == name][0],
                        recipe,
                        amount
                    )
                )

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
