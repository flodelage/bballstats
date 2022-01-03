
from django.db import models

from team.models import Team

class Game(models.Model):
    date = models.DateField(auto_now_add=True)

    opponent = models.CharField(
        max_length=128
    )

    opponent_points = models.PositiveSmallIntegerField(
        verbose_name="Points de l'adversaire",
        default=0
    )

    team_points = models.PositiveSmallIntegerField(
        verbose_name="Points de l'équipe",
        default=0
    )

    comment = models.TextField(null=True)

    PLACE_CHOICES = [
        ('home', 'à domicile'),
        ('away', "à l'extérieur"),
        ('neutral', 'sur terrain neutre')
    ]
    place = models.CharField(
        max_length=7,
        choices=PLACE_CHOICES,
        default='neutral'
    )

    # Foreign Key(s):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="games"
    )
