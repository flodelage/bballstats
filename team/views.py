
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from player.models import Player
from .models import Team
from .forms import TeamCreateForm


@login_required
def team_create(request, username):
    """
    Allow a user to create team
    """
    username = request.user.username
    team_form = TeamCreateForm()
    if request.method == 'POST':
        team_form = TeamCreateForm(request.POST)
        if team_form.is_valid():
            team_form.save()
            return redirect('home')
    return render(
        request,
        'team/team-create.html',
        {'username':username, 'team_form': team_form}
    )


@login_required
def teams_list(request, username):
    teams = Team.objects.filter(profile__pk=request.user.pk)
    return render(
        request,
        'team/teams-list.html',
        {'username':username, 'teams': teams}
    )


@login_required
def team_detail(request, username, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    players = Player.objects.filter(team__pk=team_pk)
    return render(
        request,
        'team/team-detail.html',
        {'username':username, 'team': team, 'players': players}
    )

