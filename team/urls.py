
from django.urls import path
from team import views


urlpatterns = [
    path('create/', views.team_create, name='team_create'),
    path('teams/', views.teams_list, name='teams_list'),
    path('<str:team_name>/', views.team_detail, name='team_detail'),
]