
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import PlayerCreateForm
from team.models import Team
from .models import Player


@login_required
def player_create(request, username, team_pk):
    player_form = PlayerCreateForm()
    if request.method == 'POST':
        player_form = PlayerCreateForm(request.POST)
        if player_form.is_valid():
            player = Player(
                first_name=player_form.cleaned_data['first_name'],
                last_name=player_form.cleaned_data['last_name'],
                jersey_number=player_form.cleaned_data['jersey_number'],
                picture=player_form.cleaned_data['picture']
            )
            player.team = get_object_or_404(Team, pk=team_pk)
            player.save()
            return redirect(reverse('players_list', kwargs={'username': username, 'team_pk': team_pk}))
    return render(
        request,
        'player/player-create.html',
        {
            'username': username,
            'team_pk': team_pk,
            'player_form': player_form
        }
    )


@login_required
def players_list(request, username, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    players = Player.objects.filter(team__pk=team_pk)
    return render(
        request,
        'player/players-list.html',
        {
            'username': username,
            'players': players,
            'team_pk': team_pk
        }
    )


@login_required
def player_delete(request, username, team_pk, player_pk):
    get_object_or_404(Player, pk=player_pk).delete()
    return redirect(reverse('players_list', kwargs={'username': username, 'team_pk': team_pk}))
