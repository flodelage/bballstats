
from django import forms

from team.models import Team


class TeamCreateForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ('club_name', 'city', 'province', 'level', 'picture')
