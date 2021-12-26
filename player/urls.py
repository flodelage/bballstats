
from django.urls import path
from player import views


urlpatterns = [
    path('<int:team_pk>/players/', views.players_list, name='players_list'),
]
