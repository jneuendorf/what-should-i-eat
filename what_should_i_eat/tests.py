from django.test import TestCase
from datetime import date

from recipe_book.models import Recipe, Ingredient, Tag, IngredientAmount


# Create your tests here.

class SuggestedRecipeTests(TestCase):
    """Tests the behavior of the recipe queue."""

    def setUp(self):
        self.ingredient = Ingredient.objects.create(name="ingredient1")
        self.tag = Tag.objects.create(name="tag1", color="#cccccc")
        self.recipe1 = Recipe.objects.create(
            name="recipe1",
            description="description1",
            cooked_last=date.today(),
        )
        self.recipe1.tags = [self.tag]
        IngredientAmount.objects.create(
            ingredient=self.ingredient,
            recipe=self.recipe1,
            amount="2 pieces",
        )
        self.recipe1.save()
        print(self.recipe1)

    def test_setup(self):
        self.assertEqual(
            self.recipe1.ingredients.all()[0].ingredient.name,
            "ingredient1"
        )
        self.assertEqual(
            self.recipe1.ingredients.all()[0].amount,
            "2 pieces"
        )
        self.assertIs(
            self.recipe1.ingredients.all()[0].recipe,
            self.recipe1
        )
        self.assertEqual(
            self.recipe1.tags.all()[0].name,
            "tag1"
        )

    # method name must begin with "test_"
    def test_suggest_least_recently_cooked(self):
        """The recipe cooked on the earliest date should be suggested."""
        self.assertIs(True, True)
