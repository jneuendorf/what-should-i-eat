from django.test import TestCase
from datetime import date

from recipe_book.models import Recipe, Ingredient, Tag, IngredientAmount


# Create your tests here.

class SuggestedRecipeTests(TestCase):
    """Tests the behavior of the recipe queue."""

    def setUp(self):
        ingredient = Ingredient.objects.create()
        ingredient_amout = IngredientAmount.objects.create(
            ingredient=ingredient,
            recipe=None,
            amount=2,
        )
        tag = Tag.objects.create(name="tagname", color="#cccccc")
        self.a = Recipe.objects.create(
            name="a",
            # ingredients=[ingredient],
            description="...",
            cooked_last=date.today(),
            tags=[tag],
        )

    # method name must begin with "test_"
    def test_suggest_least_recently_cooked(self):
        """The recipe cooked on the earliest date should be suggested."""
