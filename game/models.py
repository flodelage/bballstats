
from django.db import models

from team.models import Team

class Game(models.Model):
    date = models.DateField(
        verbose_name="Date",
        auto_now_add=True
    )

    opponent = models.CharField(
        verbose_name="Adversaire",
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

    comment = models.TextField(
        verbose_name="Commentaire",
        null=True)

    PLACE_CHOICES = [
        ('à domicile', 'à domicile'),
        ("à l'extérieur", "à l'extérieur"),
        ('sur terrain neutre', 'sur terrain neutre')
    ]
    place = models.CharField(
        verbose_name="Lieu",
        max_length=18,
        choices=PLACE_CHOICES,
        default='à domicile'
    )

    @property
    def victory(self):  # sourcery skip: boolean-if-exp-identity
        """
        Set if team won or not
        """
        return True if self.opponent_points < self.team_points else False

    # Foreign Key(s):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="games"
    )
