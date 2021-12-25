
from django.db import models
from django.conf import settings

from team.models import Team


class Player(models.Model):
    first_name = models.CharField(
        'Prénom',
        max_length=128
    )
    last_name = models.CharField(
        'Nom de famille',
        max_length=128
    )
    jersey_number = models.CharField(
        'Numéro de maillot',
        max_length=2
    )
    picture = models.ImageField(
        'Photo',
        null=True
    )

    # Foreign Key(s):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="players"
    )

    def __str__(self):
        return f"Joueur {self.pk}/ {self.first_name} {self.last_name} #{self.jersey_number}\nMembre de l'équipe: {self.team.club_name}"
