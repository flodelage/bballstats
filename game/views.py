
from django.shortcuts import render

from .models import Game


def games_list(request, username, team_pk):
    username = request.user.username
    games = Game.objects.filter(team__pk=team_pk)
    return render(
        request,
        'game/games-list.html',
        {'username': username, 'games': games}
    )
