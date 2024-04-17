from django import forms

from tasty.accounts.models import Profile


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef']

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'first_name', 'last_name', 'chef', 'bio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)