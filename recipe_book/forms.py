from django import forms

from .models import Recipe

# class AddRecipeForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)

# Create the form class.
class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        # fields = ['pub_date', 'headline', 'content', 'reporter']
        fields = '__all__'
