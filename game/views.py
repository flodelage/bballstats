
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Game
from.forms import GameUpdateForm
from team.models import Team
from statistic.models import Statistic
from statistic.utils.team_totals_calculator import TeamTotalsCalculator


def game_detail(request, username, team_pk, game_pk):
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


@login_required
def game_update(request, username, team_pk, game_pk):
    game = get_object_or_404(Game, pk=game_pk)
    if request.method == 'POST':
        update_form = GameUpdateForm(request.POST, instance=game)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse('team_detail', kwargs={'username': username, 'team_pk': team_pk}))
    else:
        update_form = GameUpdateForm(instance=game)
    return render(
        request,
        'game/game-update.html',
        {'update_form': update_form, 'username': username, 'game': game}
    )


@login_required
def game_delete(request, username, team_pk, game_pk):
    pass
    # get_object_or_404(Player, pk=player_pk).delete()
    # return redirect(reverse('players_list', kwargs={'username': username, 'team_pk': team_pk}))
