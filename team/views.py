
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from player.models import Player
from account.models import Profile
from .models import Team
from .forms import TeamCreateForm


@login_required
def team_create(request, username):
    """
    Allow a user to create team
    """
    team_form = TeamCreateForm()
    if request.method == 'POST':
        team_form = TeamCreateForm(request.POST)
        if team_form.is_valid():
            team = Team(
                club_name=team_form.cleaned_data['club_name'],
                city=team_form.cleaned_data['city'],
                province=team_form.cleaned_data['province'],
                level=team_form.cleaned_data['level'],
                picture=team_form.cleaned_data['picture']
            )
            team.profile = get_object_or_404(Profile, pk=request.user.id)
            team.save()
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

