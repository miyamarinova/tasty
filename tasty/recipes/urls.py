from django.urls import path

from tasty.recipes.views import (CatalogueView, CreateRecipeView, DetailsRecipeView,
                                 EditRecipeView, DeleteRecipeView)


urlpatterns=[
    path('catalogue/', CatalogueView.as_view(), name='catalogue'),
    path('create/', CreateRecipeView.as_view(), name='create recipe'),
    path('<int:pk>/detail/', DetailsRecipeView.as_view(), name="details recipe"),
    path('<int:pk>/edit/', EditRecipeView.as_view(), name='edit recipe'),
    path('<int:pk>/delete/', DeleteRecipeView.as_view(), name='delete recipe')
]