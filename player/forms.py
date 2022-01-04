
from django import forms

from player.models import Player


class PlayerCreateForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ('first_name', 'last_name', 'jersey_number', 'picture')
