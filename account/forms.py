
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms


class ProfileCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)


class ProfileChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email',)


class ProfileLoginForm(forms.Form):
    email = forms.CharField(max_length=128, label='Email')
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, label='Mot de passe')
