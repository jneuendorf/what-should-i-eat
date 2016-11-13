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
        "id": "tags",
        "items": [
            {
                "class": "class-a",
                "value": "a",
                "text": "1st item"
            }
        ],
        "add_item": "click me",
        # "js": False,
        "js": {
            "suggestions": ["asdf", "bsdf"]
        },
    }))
    images = forms.FileField()
