
from django.db import models
from django.conf import settings
import datetime


class Team(models.Model):
    club_name = models.CharField(
        verbose_name='Nom du club',
        max_length=128
    )

    city = models.CharField(
        verbose_name='Ville',
        max_length=128
    )

    province = models.CharField(
        verbose_name='Département',
        max_length=128
    )

    GENRE_CHOICES = [
        ('féminine', 'féminine'),
        ('masculine', 'masculine')
    ]
    genre = models.CharField(
        max_length=9,
        choices=GENRE_CHOICES,
        default='féminine'
    )

    level = models.CharField(
        verbose_name='Niveau',
        max_length=128
    )

    SEASON_CHOICES = [
        (f'{year}-{year+1}', f'{year}-{year+1}')
        for year in range(datetime.datetime.now().year-1, datetime.datetime.now().year+2)
    ]
    season = models.CharField(
        max_length=9,
        choices=SEASON_CHOICES,
        default=SEASON_CHOICES[1][0]
    )

    picture = models.ImageField(
        verbose_name='Photo',
        blank=True,
        null=True
    )

    # Foreign Key(s):
    profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Équipe {self.pk}/ {self.club_name} ({self.city}, {self.province}) - {self.level}\nÉquipe de: {self.profile.username}"
