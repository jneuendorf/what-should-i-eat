from datetime import date, timedelta
# from itertools import chain

from django import forms
from django.forms import modelformset_factory

from static_precompiler.utils import compile_static

import fuelux_widgets
from .models import Recipe, Tag, Ingredient, Image


class AddRecipeForm(forms.ModelForm, fuelux_widgets.FuelUxForm):
    class Meta:
        model = Recipe
        fields = [
            'name',
            'description',
        ]

    # FIELDS
    ingredients = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": (
                    "comma separated list, "
                    "e.g. 1 carrot, 2 slices of cucumber"
                )
            }
        )
    )
    ingredients_choices = forms.CharField(
        label="",
        required=False,
        widget=fuelux_widgets.Pillbox(
            attrs={
                "add_item": "",
                "js": {
                    "edit": False,
                    "readonly": True,
                },
            }
        )
    )
    tags = forms.CharField(
        required=False,
        widget=fuelux_widgets.Pillbox(
            attrs={
                "add_item": "add tags",
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

    # MISC SETTINGS

    field_order = [
        "name",
        "ingredients",
        "ingredients_choices",
        "description",
        "tags",
        "images",
        "cooked_last",
    ]

    # CONSTRUCTOR
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tags"].widget.set_suggestions(
            Tag.objects.all()
        )
        self.fields["ingredients_choices"].widget.set_items(
            {
                "text": ingredient,
                "value": ingredient,
                "class": "ingredient-choice",
            }
            for ingredient in Ingredient.objects.all()
        )


class RecipeImageFormSet(modelformset_factory(Image, fields=('image',))):

    def __init__(self, *args, **kwargs):
        kwargs["prefix"] = "recipe_image"
        super().__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        for form in self:
            print("would save form", form)
            # TODO
            # form.save(*args, **kwargs)
        return self


# This is closured in django.forms.widgets...
# MEDIA_TYPES = ('css', 'js')


# Media class with support for coffescript ({% path/to/file.coffee|compile %})
# class CompiledMedia(forms.Media):
#
#     # like render() but only outputting the path to the media file
#     def paths(self):
#         return chain(*[
#             getattr(self, name + '_paths')()
#             for name in MEDIA_TYPES
#         ])
#
#     def js_paths(self):
#         return [self.absolute_path(path) for path in self._js]
#
#     def css_paths(self):
#         print(">>>>", self._css.keys())
#         media = sorted(self._css.keys())
#         return chain(*[
#             [self.absolute_path(path) for path in self._css[medium]]
#             for medium in media
#         ])

# This is necessary because django does not support
# setting the media object as inner class definition for form sets
# Possible would be to create a form with a media class
# and derive the form set from that form.
# But this way we can't use the 'modelformset_factory'.
RecipeImageFormSet.media = forms.Media(
    # relative to static url
    js=(
        # TODO: this does not need to be compiled once done!
        # compile_static("shared/js/formset_actions.coffee"),
        "shared/js/jquery.formset.js",
        compile_static("recipe_book/js/init_formset.coffee")
    )
)
# RecipeImageFormSet.media = CompiledMedia(
#     # relative to static url
#     js=("recipe_book/js/formset_add_remove.coffee",)
# )
