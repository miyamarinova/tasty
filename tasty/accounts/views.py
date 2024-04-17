from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from tasty.accounts.forms import CreateProfileForm, EditProfileForm
from tasty.accounts.models import Profile
from tasty.recipes.models import Recipe


def get_profile(request):
    return Profile.objects.first()

# Create your views here.
class CreateProfileView(views.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'profile/create-profile.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):

        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)

class DetailsProfileView(views.DetailView):
    model = Profile
    template_name = 'profile/details-profile.html'  # Replace 'profile_details.html' with your actual template name
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_profile(self.request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Count the number of published recipes
        published_recipe_count = Recipe.objects.filter().count()
        # Add the count to the context
        context['published_recipe_count'] = published_recipe_count
        return context

class EditProfileView(views.UpdateView):
    model = Profile
    form_class = EditProfileForm
    template_name = 'profile/edit-profile.html'
    success_url = reverse_lazy('details profile')

    def get_object(self, queryset=None):
        return get_profile(self.request)

class DeleteProfileView(views.DeleteView):
    model = Profile
    template_name = 'profile/delete-profile.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return get_profile(self.request)