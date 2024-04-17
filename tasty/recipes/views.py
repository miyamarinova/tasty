from urllib import request

from django import forms
from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from tasty.accounts.models import Profile
from tasty.recipes.forms import CreateRecipeForm, EditRecipeForm
from tasty.recipes.models import Recipe

def get_profile(request):
    return Profile.objects.first()

# Create your views here.
class CatalogueView(views.ListView):
    model = Recipe
    template_name = 'recipe/catalogue.html'
    context_object_name = 'recipes'

    def get(self, request, *args, **kwargs):
        # Call the super().get() method to execute the default behavior of the ListView class
        response = super().get(request, *args, **kwargs)

        # Get the user's profile using the get_profile() function
        profile = get_profile(request)

        # Add the profile to the context dictionary
        response.context_data['profile'] = profile

        return response

class CreateRecipeView(views.CreateView):
    model = Recipe
    form_class = CreateRecipeForm
    template_name = 'recipe/create-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        profile = get_profile(request)
        if profile:
            form.instance.author = profile
            return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile(request)
        return context

class DetailsRecipeView(views.DetailView):
    queryset = Recipe.objects.all()
    template_name = "recipe/details-recipe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_profile(request)
        recipe = self.object
        ingredients_list = recipe.ingredients.split(', ')
        context['ingredients_list'] = ingredients_list
        return context

class EditRecipeView(views.UpdateView):
    model = Recipe
    form_class = EditRecipeForm
    template_name = 'recipe/edit-recipe.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class DeleteRecipeView(views.DeleteView):
    queryset = Recipe.objects.all()
    template_name = 'recipe/delete-recipe.html'
    fields = ['title', 'cuisine_type', 'ingredients', 'instructions',
              'cooking_time', 'image_url']
    success_url = reverse_lazy('catalogue')
    form_class = modelform_factory(
        Recipe,
        fields=['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time',
                'image_url'],
    )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["instance"] = self.object
        return kwargs