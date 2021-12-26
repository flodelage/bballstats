
from django.db import models


class Game(models.Model):
    date = models.DateField(auto_now_add=True)
    opponent = models.CharField(
        max_length=128
    )
    opponent_points = models.PositiveSmallIntegerField(
        verbose_name="Points de l'adversaire",
        default=0
    )
    comment = models.TextField(null=True)
