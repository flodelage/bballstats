
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Team
from .forms import TeamCreateForm


@login_required
def team_create(request):
    """
    Allow a user to create team
    """
    team_form = TeamCreateForm()
    if request.method == 'POST':
        team_form = TeamCreateForm(request.POST)
        if team_form.is_valid():
            team_form.save()
            return redirect('home')
    return render(
        request,
        'team/team-create.html',
        {'username':request.user.username, 'team_form': team_form}
    )


@login_required
def teams_list(request):
    teams = Team.objects.filter(profile__pk=request.user.pk)
    return render(
        request,
        'team/teams-list.html',
        {'username':request.user.username, 'teams': teams}
    )


@login_required
def team_detail(request, club_name):
    team = get_object_or_404(Team, club_name=club_name)
    players = Player.objects.filter(team__pk=team.pk)
    return render(
        request,
        'team/team-detail.html',
        {'username':request.user.username, 'team': team, 'players': players}
    )

