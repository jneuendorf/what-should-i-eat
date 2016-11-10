from django.test import TestCase
import datetime

from recipe_book.models import Recipe, Ingredient, Tag, IngredientAmount
from .views import suggest_recipe


# Create your tests here.

class SuggestedRecipeTests(TestCase):
    """Tests the behavior of the recipe queue."""

    def setUp(self):
        self.ingredient1_name = "ingredient1"
        self.tag1_name = "tag1"
        self.recipe1_name = "recipe1"
        self.recipe1_desc = "description1"
        self.ingredient_amount1_amount = "2 pieces"

        self.ingredient1 = Ingredient.objects.create(
            name=self.ingredient1_name
        )
        self.tag1 = Tag.objects.create(
            name=self.tag1_name,
            color="#cccccc"
        )
        self.recipe1 = Recipe.objects.create(
            name=self.recipe1_name,
            description=self.recipe1_desc,
            cooked_last=datetime.date.today(),
        )
        self.recipe1.tags = [self.tag1]
        IngredientAmount.objects.create(
            ingredient=self.ingredient1,
            recipe=self.recipe1,
            amount=self.ingredient_amount1_amount,
        )
        self.recipe1.save()

    def test_setup(self):
        self.assertEqual(
            self.recipe1.ingredients.all()[0].name,
            self.ingredient1_name
        )
        self.assertEqual(
            self.recipe1.ingredient_amounts.all()[0].amount,
            self.ingredient_amount1_amount
        )
        self.assertIs(
            self.recipe1.ingredient_amounts.all()[0].recipe,
            self.recipe1
        )
        self.assertEqual(
            self.recipe1.tags.all()[0].name,
            self.tag1_name
        )

    # method name must begin with "test_"
    def test_suggest_least_recently_cooked(self):
        """
        The recipe cooked on the earliest date should be suggested.
        If several recipes have been cooked on the same day then
        the recipe with the highest priority should be suggested.
        If several recipes have the same priority then any recipe
        may be suggested.
        """
        recipe_yesterday = Recipe.objects.create(
            name="recipe_yesterday",
            description="...",
            cooked_last=datetime.date.today() - datetime.timedelta(days=1),
        )
        recipe_yesterday.tags = [self.tag1]
        IngredientAmount.objects.create(
            ingredient=self.ingredient1,
            recipe=recipe_yesterday,
            amount="2 ml",
        )

        # self.recipe1 has been cooked today => expect recipe_yesterday
        self.assertEqual(
            suggest_recipe(
                recipes=Recipe.objects.all(),
                tags=Tag.objects.all(),
                ingredients=Ingredient.objects.all(),
            ),
            recipe_yesterday
        )

        # 2 recipes cooked on the same day => priority sorting
        recipe_yesterday2 = Recipe.objects.create(
            name="recipe_yesterday2",
            description="...",
            cooked_last=datetime.date.today() - datetime.timedelta(days=1),
            priority=recipe_yesterday.priority + 1,
        )
        recipe_yesterday2.tags = [self.tag1]
        IngredientAmount.objects.create(
            ingredient=self.ingredient1,
            recipe=recipe_yesterday2,
            amount="500 g",
        )

        # self.recipe1 has been cooked today => expect recipe_yesterday
        self.assertEqual(
            suggest_recipe(
                recipes=Recipe.objects.all(),
                tags=Tag.objects.all(),
                ingredients=Ingredient.objects.all(),
            ),
            recipe_yesterday2
        )

    def test_suggested_has_tag_or_ingredient(self):
        """
        The suggested recipe should have at least 1 tag or ingredient
        in common with the tags and ingredients provided by the filter.
        """
        self.assertIs(
            suggest_recipe(
                recipes=Recipe.objects.all(),
                tags=set(),
                ingredients=set(),
            ),
            None
        )

        tags = set(Tag.objects.all())
        ingredients = set(Ingredient.objects.all())

        while True:
            suggested_recipe = suggest_recipe(
                recipes=Recipe.objects.all(),
                tags=tags,
                ingredients=ingredients,
            )

            self.assertTrue(
                set(suggested_recipe.tags.all()) <= tags or
                set(suggested_recipe.ingredients.all()) <= ingredients
                # {ingredient_amount.ingredient
                #  for ingredient_amount in suggested_recipe.ingredients.all()}
                # <= ingredients
            )

            if len(tags) > 0:
                tags.pop()
            else:
                ingredients.pop()
            if len(tags) == 0 and len(ingredients) == 0:
                break
