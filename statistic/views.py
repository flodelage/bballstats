
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from team.models import Team
from player.models import Player
from game.models import Game
from statistic.models import Statistic
from statistic.utils.team_totals_calculator import TeamTotalsCalculator
from statistic.utils.team_averages_calculator import TeamAveragesCalculator
from statistic.utils.players_averages_calculator import PlayersAveragesCalculator


def players_averages(request, username, team_pk):
    players = Player.objects.filter(team__pk=team_pk)
    games = Game.objects.filter(team__pk=team_pk)
    players_stats = Statistic.objects.filter(
        game__pk__in=[game.id for game in games]
    )

    players_averages_calculator = PlayersAveragesCalculator()

    players_stats_with_averages = sorted(
        players_averages_calculator.final_stats(players, players_stats),
        key=lambda stats: stats['stats_averages']['points_avg'],
        reverse=True
    )

    return render(
        request,
        'statistic/players-averages.html',
        {
            'username': username,
            'team_pk': team_pk,
            'games': games,
            'players_stats': players_stats_with_averages,
        }
    )


def team_averages(request, username, team_pk):
    games = Game.objects.filter(team__pk=team_pk)
    players_stats = Statistic.objects.filter(
        game__pk__in=[game.id for game in games]
    )

    team_totals_calculator = TeamTotalsCalculator()
    team_stats = team_totals_calculator.add_players_statistics(players_stats)
    team_averages_calculator = TeamAveragesCalculator()
    team_averages = team_averages_calculator.team_averages(
        team_stats, len(games)
    )

    return render(
        request,
        'statistic/team-averages.html',
        {
            'username': username,
            'team_pk': team_pk,
            'games': games,
            'team_averages': team_averages
        }
    )
