
from django.urls import path
from statistic import views


# urls start with: account/<str:username>/team/<int:team_pk>/
urlpatterns = [
    path('players-averages/', views.players_averages, name='players_averages'),
    path('team-averages/', views.team_averages, name='team_averages'),
]