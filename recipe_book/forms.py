from django import forms

from .models import Recipe


# Create the form class.
class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # fields = ['pub_date', 'headline', 'content', 'reporter']
        fields = '__all__'
