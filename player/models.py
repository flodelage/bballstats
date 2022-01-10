
from django.db import models
from django.conf import settings

from team.models import Team

from cloudinary.models import CloudinaryField


class Player(models.Model):
    first_name = models.CharField(
        verbose_name='Prénom',
        max_length=128
    )

    last_name = models.CharField(
        verbose_name='Nom de famille',
        max_length=128
    )

    JERSEY_CHOICES = [
        (str(number), str(number)) for number in range(0, 100)
    ]
    jersey_number = models.CharField(
        verbose_name="Numéro",
        max_length=2,
        choices=JERSEY_CHOICES,
        default='1'
    )

    picture = CloudinaryField(
        verbose_name='Photo',
        null=True,
        blank=True
    )

    # Foreign Key(s):
    team = models.ForeignKey(
        Team,
        on_delete=models.CASCADE,
        related_name="players"
    )

    def __str__(self):
        return f"Joueur {self.pk}/ {self.first_name} {self.last_name} #{self.jersey_number}\nMembre de l'équipe: {self.team.club_name}"

    class Meta:
        unique_together = (
            ('team', 'first_name', 'last_name'),
            ('team', 'jersey_number')
        )
