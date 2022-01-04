
from django.db import models
from django.conf import settings

from team.models import Team


class Player(models.Model):
    first_name = models.CharField(
        verbose_name='Prénom',
        max_length=128
    )

    last_name = models.CharField(
        verbose_name='Nom de famille',
        max_length=128
    )

    jersey_number = models.CharField(
        verbose_name='Numéro de maillot',
        max_length=2
    )

    picture = models.ImageField(
        verbose_name='Photo',
        blank=True,
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
