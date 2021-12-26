
from django.db import models


class Game(models.Model):
    date = models.DateField()
    opponent = models.CharField(
        max_length=128
    )
    final_score = models.CharField(
        max_length=128
    )
    comment = models.TextField(null=True)
