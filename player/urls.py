
from django.urls import path
from player import views


# urls start with: account/<str:username>/team/<int:team_pk>/players/
urlpatterns = [
    path('', views.players_list, name='players_list'),
    path('create/', views.player_create, name='player_create'),
    path('<int:player_pk>/delete/', views.player_delete, name='player_delete'),
]
