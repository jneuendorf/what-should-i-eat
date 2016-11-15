from datetime import date, timedelta
from django import forms

import fuelux_widgets
from .models import Recipe, Tag, Ingredient


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
    ingredients = forms.CharField(widget=fuelux_widgets.Pillbox(
        attrs={
            "add_item": "add ingredients",
        }
    ))
    tags = forms.CharField(
        required=False,
        widget=fuelux_widgets.Pillbox(
            attrs={
                "add_item": "add tags",
            }
        )
    )
    images = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True
            }
        )
    )
    cooked_last = forms.DateField(
        required=False,
        widget=fuelux_widgets.Datepicker(
            attrs={
                "style": "width: 300px;",
                "js": {
                    "allow_past_dates": True,
                    "restricted": (
                        "[{{from: '{}', to: Infinity}}]".format(
                            "{:%Y-%m-%d}".format(
                                date.today() + timedelta(days=1)
                            )
                        )
                    ),
                    "moment_config": {
                        "culture": "en",
                        "format": "YYYY-MM-DD"
                    },
                },
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tags"].widget.set_suggestions(
            Tag.objects.all()
        )
        self.fields["ingredients"].widget.set_suggestions(
            Ingredient.objects.all()
        )
