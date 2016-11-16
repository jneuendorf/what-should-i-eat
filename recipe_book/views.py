# from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render

from .models import Recipe, Tag
from .forms import AddRecipeForm


# Create your views here.

def index(request):
    recipes = Recipe.objects.order_by('name')
    return render(request, 'recipe_book/index.html', {
        'title': 'recipe book',
        'recipes': recipes,
    })


def add(request):
    # import pdb; pdb.set_trace()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddRecipeForm(request.POST)
        # print("form data:", form.data)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print("form data:", form.data)
            print("form cleaned data:", form.cleaned_data)

            # directly applicable
            done = ["name", "description"]

            # form cleaned data: {'ingredients_choices': '', 'name': 'test recipe', 'description': 'adsf', 'ingredients': '50 g Butter', 'cooked_last': datetime.date(2016, 11, 16), 'images': None, 'tags': 'Italian,'}

            # ingredient1_name = "ingredient1"
            # tag1_name = "tag1"
            # recipe1_name = "recipe1"
            # recipe1_desc = "description1"
            # ingredient_amount1_amount = "2 pieces"
            #
            # ingredient1 = Ingredient.objects.create(
            #     name=ingredient1_name
            # )
            # tag1 = Tag.objects.create(
            #     name=tag1_name,
            #     color="#cccccc"
            # )
            # recipe1 = Recipe.objects.create(
            #     name=recipe1_name,
            #     description=recipe1_desc,
            #     cooked_last=datetime.date.today(),
            # )
            # recipe1.tags = [tag1]
            # IngredientAmount.objects.create(
            #     ingredient=ingredient1,
            #     recipe=recipe1,
            #     amount=ingredient_amount1_amount,
            # )
            # recipe1.save()


            # form = AddRecipeForm()

            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
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
