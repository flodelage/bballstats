
from django.shortcuts import render


def games_list(request, username, team_pk):
    username = request.user.username
    games = Game.objects.filter()
