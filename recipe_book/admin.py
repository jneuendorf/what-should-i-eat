from django.contrib import admin
from .models import Recipe, Tag, Image, Ingredient, IngredientAmount


# Register your models here.

# class RecipeAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]
#     inlines = [ChoiceInline]
#
# admin.site.register(Recipe, RecipeAdmin)

admin.site.register(Recipe)
admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Ingredient)
admin.site.register(IngredientAmount)
