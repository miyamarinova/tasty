from django import forms

from tasty.recipes.models import Recipe


class CreateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions',
                  'cooking_time', 'image_url']

        labels = {
            'title': 'Title',
            'cuisine_type': 'Cuisine Type',
            'ingredients': 'Ingredients',
            'instructions': 'Instructions',
            'cooking_time': 'Cooking Time (minutes)',
            'image_url': 'Image URL',
        }
        widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter recipe title'}
            ),

            'ingredients': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'ingredient1, ingredient2, ...'}
            ),
            'instructions': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Enter detailed instructions here...'}
            ),

            'image_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Optional image URL here...'}
                                         ),
        }

class EditRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)