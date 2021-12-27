
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

    @property
    def points(self):
        """
        Calculate total points from different shots made
        """
        return ((self.field_goals_made - self.three_points_made)*2) + (self.three_points_made*3) + (self.free_throws_made*1)

    @property
    def field_goals_percent(self):
        """
        Calculate field goal percent from
        3pts and 2pts shots
        """
        try:
            return round((self.field_goals_made / self.field_goals_attempted) *100, 1)
        except ZeroDivisionError:
            return 0.0

    @property
    def three_points_percent(self):
        """
        Calculate field goal percent from
        3pts shots
        """
        try:
            return round((self.three_points_made / self.three_points_attempted) *100, 1)
        except ZeroDivisionError:
            return 0.0

    @property
    def free_throws_percent(self):
        """
        Calculate field goal percent from
        free throws shots
        """
        try:
            return round((self.free_throws_made / self.free_throws_attempted) *100, 1)
        except ZeroDivisionError:
            return 0.0

    @property
    def rebounds(self):
        """
        Calculate total rebounds from
        offensive and defensive rebounds
        """
        return self.offensive_rebounds + self.defensive_rebounds
