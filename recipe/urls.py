from django.urls import path
from .views import *



urlpatterns = [
    path('v1/ingredient', IngredientList),
    path('v1/category/<int:cat_id>' , IngredientDetail),
    path('v1/recipe', RecipeList),
    path('v1/recipe/<int:product_id>' ,RecipeDetail)
]
