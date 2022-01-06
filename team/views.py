
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from account.models import Profile
from player.models import Player
from game.models import Game
from .models import Team
from statistic.models import Statistic
from statistic.utils.players_averages_calculator import PlayersAveragesCalculator
from statistic.utils.team_leaders_calculator import TeamLeadersCalculator
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
                genre=team_form.cleaned_data['genre'],
                season=team_form.cleaned_data['season'],
                picture=team_form.cleaned_data['picture']
            )
            team.profile = get_object_or_404(Profile, pk=request.user.id)
            team.save()
            return redirect(reverse('players_list', kwargs={'username': username, 'team_pk': team.pk}))
    return render(
        request,
        'team/team-create.html',
        {'username':username, 'team_form': team_form}
    )


@login_required
def teams_list(request, username):
    teams = Team.objects.filter(profile__pk=request.user.pk).order_by('-season')
    return render(
        request,
        'team/teams-list.html',
        {'username':username, 'teams': teams}
    )


def team_detail(request, username, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    games = Game.objects.filter(team__pk=team_pk)
    context = {
        'username':username,
        'team': team,
        'games': games
    }
    if games:
        players = Player.objects.filter(team__pk=team_pk)
        players_stats = Statistic.objects.filter(game__pk__in=[game.id for game in games])

        players_averages_calculator = PlayersAveragesCalculator()
        players_stats_with_averages = players_averages_calculator.final_stats(players, players_stats)

        team_leaders_calculator = TeamLeadersCalculator()
        team_leaders = team_leaders_calculator.set_team_leaders(players_stats_with_averages)
        context['team_leaders'] = team_leaders
    return render(
        request,
        'team/team-detail.html',
        context
    )


@login_required
def team_update(request, username, team_pk):
    team = get_object_or_404(Team, pk=team_pk)
    if request.method == 'POST':
        update_form = TeamCreateForm(request.POST, instance=team)
        if update_form.is_valid():
            update_form.save()
            return redirect(reverse('teams_list', kwargs={'username': username}))
    else:
        update_form = TeamCreateForm(instance=team)
    return render(
        request,
        'team/team-update.html',
        {'update_form': update_form, 'username': username, 'team': team}
    )


@login_required
def team_delete(request, username, team_pk):
    get_object_or_404(Team, pk=team_pk).delete()
    return redirect(reverse('teams_list', kwargs={'username': username}))


@login_required
def team_select(request, username):
    teams = Team.objects.filter(profile__pk=request.user.pk).order_by('season')
    if teams:
        return render(
            request,
            'team/team-select.html',
            {'username': username, 'teams': teams}
        )
    else:
        return redirect(reverse('team_create', kwargs={'username': username}))
