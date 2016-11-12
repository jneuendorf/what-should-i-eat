from django import forms

import fuelux_widgets
from .models import Recipe


# Create the form class.
class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'name',
            # ingredients here only for field ordering (is overridden below)
            'ingredients',
            'description',
            # 'cooked_last',
            # 'images',
        ]
    ingredients = forms.CharField()
    tags = forms.CharField(widget=fuelux_widgets.Pillbox(attrs={
        "items": [
            {
                "class": "class-a",
                "value": "a",
                "title": "1st item"
            }
        ],
        "suggestions": ["asdf", "bsdf"]
    }))
