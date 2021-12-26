
from django.shortcuts import render, get_object_or_404

from .models import Game
from team.models import Team
from statistic.models import Statistic


def games_list(request, username, team_pk):
    username = request.user.username
    team = get_object_or_404(Team, pk=team_pk)
    games = Game.objects.filter(team__pk=team_pk)
    return render(
        request,
        'game/games-list.html',
        {'username': username, 'team': team, 'games': games}
    )

def game_detail(request, username, team_pk, game_pk):
    username = request.user.username
    team = get_object_or_404(Team, pk=team_pk)
    game = get_object_or_404(Game, pk=game_pk)
    stats = Statistic.objects.filter(game__pk=game_pk)
    return render(
        request,
        'game/game-detail.html',
        {'username': username, 'team': team, 'game': game, 'stats':stats}
    )
