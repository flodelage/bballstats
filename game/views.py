
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Game
from.forms import GameCreateForm, GameUpdateForm
from team.models import Team
from player.models import Player
from statistic.models import Statistic
from statistic.utils.team_totals_calculator import TeamTotalsCalculator


@login_required
def game_create(request, username, team_pk):
    form = GameCreateForm()
    if request.method == 'POST':
        form = GameCreateForm(request.POST)
        if form.is_valid():
            game = Game(
                opponent = form.cleaned_data['opponent'],
                place = form.cleaned_data['place']
            )
            game.team = get_object_or_404(Team, pk=team_pk)
            game.save()
            return redirect(reverse('game_processing', kwargs={'username': username, 'team_pk': team_pk, 'game_pk': game.pk}))
    return render(
        request,
        'game/game-create.html',
        {
            'form': form,
            'username': username,
        }
    )


# @login_required
# def choose_starters(request, username, team_pk, game_pk):
#     players = Player.objects.filter(team__pk=team_pk).order_by('last_name')
#     return render(
#         request,
#         'game/game-starters.html',
#         {'username': username, 'players': players}
#     )


@login_required
def game_processing(request, username, team_pk, game_pk):
    players = Player.objects.filter(team__pk=team_pk).order_by('last_name')
    players_stats = []
    for p in players:
        s = Statistic()
        s.game = get_object_or_404(Game, pk=game_pk)
        s.player = get_object_or_404(Player, pk=p.pk)
        s.save()
        players_stats.append(s)
    return render(
        request,
        'game/game-processing.html',
        {
            'username': username,
            'players': players,
            'players_stats': players_stats
        }
    )


@login_required
def game_compute_stat(request):
    return JsonResponse({})


def game_detail_players(request, username, team_pk, game_pk):
    team = get_object_or_404(Team, pk=team_pk)
    game = get_object_or_404(Game, pk=game_pk)
    players_stats = sorted(
        Statistic.objects.filter(game__pk=game_pk),
        key=lambda stats: stats.points,
        reverse=True
    )

    return render(
        request,
        'game/game-detail-players.html',
        {
            'username': username,
            'team': team,
            'game': game,
            'players_stats':players_stats
        }
    )


def game_detail_team(request, username, team_pk, game_pk):
    team = get_object_or_404(Team, pk=team_pk)
    game = get_object_or_404(Game, pk=game_pk)
    players_stats = Statistic.objects.filter(game__pk=game_pk)

    team_totals_calculator = TeamTotalsCalculator()
    team_stats = team_totals_calculator.teams_statistics(players_stats)
    return render(
        request,
        'game/game-detail-team.html',
        {
            'username': username,
            'team': team,
            'game': game,
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
            return redirect(reverse('game_detail', kwargs={'username': username, 'team_pk': team_pk, 'game_pk': game_pk}))
    else:
        update_form = GameUpdateForm(instance=game)
    return render(
        request,
        'game/game-update.html',
        {'update_form': update_form, 'username': username, 'game': game}
    )


@login_required
def game_delete(request, username, team_pk, game_pk):
    get_object_or_404(Game, pk=game_pk).delete()
    return redirect(reverse('team_detail', kwargs={'username': username, 'team_pk': team_pk}))
