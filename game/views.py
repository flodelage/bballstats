
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Game
from team.models import Team
from statistic.models import Statistic
from statistic.utils.team_totals_calculator import TeamTotalsCalculator


@login_required
def games_list(request, username, team_pk):
    username = request.user.username
    team = get_object_or_404(Team, pk=team_pk)
    games = Game.objects.filter(team__pk=team_pk)
    return render(
        request,
        'game/games-list.html',
        {
            'username': username,
            'team': team,
            'games': games,
        }
    )

@login_required
def game_detail(request, username, team_pk, game_pk):
    username = request.user.username
    team = get_object_or_404(Team, pk=team_pk)
    game = get_object_or_404(Game, pk=game_pk)
    players_stats = Statistic.objects.filter(game__pk=game_pk)

    team_totals_calculator = TeamTotalsCalculator()
    team_stats = team_totals_calculator.teams_statistics(players_stats)

    return render(
        request,
        'game/game-detail.html',
        {
            'username': username,
            'team': team,
            'game': game,
            'players_stats':players_stats,
            'team_stats': team_stats
        }
    )
