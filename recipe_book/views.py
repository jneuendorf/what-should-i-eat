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
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            print("form data:", form.data)
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')
    # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = AddRecipeForm()
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
