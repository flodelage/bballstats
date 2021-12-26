
from django.shortcuts import render, redirect
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
def team_detail(request, team_name):
    pass

