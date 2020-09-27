from django.urls import path

from .views import RecipeListView, RecipeDetailView, CategoryListView, IngredientListView, autocomplete

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListView.as_view(), name='recipe-list'),
    path('search/', autocomplete, name='autocomplete'),
    path('recipes/<slug>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/categories/<slug>/', CategoryListView.as_view(), name='category-list'),
    path('recipes/ingredients/<slug>/', IngredientListView.as_view(), name='ingredient-list'),
]
