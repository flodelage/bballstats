
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from team.models import Team
from player.models import Player
from game.models import Game
from statistic.models import Statistic
from statistic.utils.team_totals_calculator import TeamTotalsCalculator
from statistic.utils.team_averages_calculator import TeamAveragesCalculator
from statistic.utils.players_averages_calculator import PlayersAveragesCalculator


@login_required
def averages(request, username, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    players = Player.objects.filter(team__pk=team_pk)
    games = Game.objects.filter(team__pk=team_pk)
    players_stats = Statistic.objects.filter(game__pk__in=[game.id for game in games])

    team_totals_calculator = TeamTotalsCalculator()
    team_stats = team_totals_calculator.calculate_team_statistics(players_stats)
    team_averages_calculator = TeamAveragesCalculator()
    team_averages = team_averages_calculator.team_averages(team_stats, len(games))

    players_averages_calculator = PlayersAveragesCalculator()
    players_stats_with_averages = players_averages_calculator.final_stats(players, players_stats)

    return render(
        request,
        'statistic/averages.html',
        {
            'username': username,
            'team_averages': team_averages,
            'players_stats': players_stats_with_averages
        }
    )
