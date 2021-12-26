
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from team.models import Team
from .models import Player


@login_required
def players_list(request, username, team_pk):
    username = request.user.username
    team = get_object_or_404(Team, pk=team_pk)
    players = Player.objects.filter(team__pk=team_pk)
    return render(
        request,
        'player/players-list.html',
        {'username': username, 'players': players}
    )
