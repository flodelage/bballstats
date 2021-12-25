
from django.db import models
from django.conf import settings


class Team(models.Model):
    name = models.CharField(
        'Nom du club',
        max_length=128
    )
    city = models.CharField(
        "Ville",
        max_length=128
    )
    province = models.CharField(
        'Département',
        max_length=128
    )
    level = models.CharField(
        'Niveau',
        max_length=128
    )
    picture = models.ImageField(
        'Photo',
        null=True
    )

    # Foreign Key(s):
    profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
