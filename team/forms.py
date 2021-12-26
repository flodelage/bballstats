
from django.contrib.auth import get_user_model
from django import forms


class TeamCreateForm(forms.Form):
    club_name = forms.CharField(
        label='Nom du club',
        max_length=128
    )
    city = forms.CharField(
        label='Ville',
        max_length=128
    )
    province = forms.CharField(
        label='Département',
        max_length=128
    )
    level = forms.CharField(
        label='Niveau',
        max_length=128
    )
    picture = forms.ImageField(
        label='Photo',
        required=False
    )
