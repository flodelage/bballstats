
from django.db import models

from player.models import Player
from game.models import Game


class Statistic(models.Model):
    minutes = models.PositiveSmallIntegerField(
        verbose_name='Minutes jouées',
        default=0
    )
    field_goals_made = models.PositiveSmallIntegerField(
        verbose_name='Tirs réussis',
        default=0
    )
    field_goals_attempted = models.PositiveSmallIntegerField(
        verbose_name='Tirs tentés',
        default=0
    )
    three_points_made = models.PositiveSmallIntegerField(
        verbose_name='3pts réussis',
        default=0
    )
    three_points_attempted = models.PositiveSmallIntegerField(
        verbose_name='3pts ratés',
        default=0
    )
    free_throws_made = models.PositiveSmallIntegerField(
        verbose_name='LF tentés',
        default=0
    )
    free_throws_attempted = models.PositiveSmallIntegerField(
        verbose_name='LF tentés',
        default=0
    )
    offensive_rebounds = models.PositiveSmallIntegerField(
        verbose_name='Rebonds offensifs',
        default=0
    )
    defensive_rebounds = models.PositiveSmallIntegerField(
        verbose_name='Rebonds défensifs',
        default=0
    )
    assists = models.PositiveSmallIntegerField(
        verbose_name='Passes décisives',
        default=0
    )
    steals = models.PositiveSmallIntegerField(
        verbose_name='Interceptions',
        default=0
    )
    blocks = models.PositiveSmallIntegerField(
        verbose_name='Contres',
        default=0
    )
    turnovers = models.PositiveSmallIntegerField(
        verbose_name='Ballons perdus',
        default=0
    )
    fouls = models.PositiveSmallIntegerField(
        verbose_name='Fautes',
        default=0
    )

    # Foreign Key(s):
    player = models.ForeignKey(
        Player,
        on_delete=models.CASCADE,
        related_name="statistics"
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="statistics"
    )
