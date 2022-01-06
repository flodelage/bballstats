

from django import forms

from game.models import Game


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('opponent', 'place')


class GameUpdateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('team_points', 'opponent', 'opponent_points', 'place', 'comment')
