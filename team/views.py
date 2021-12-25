
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Team


@login_required
def team_create(request):
    pass


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

