
from django.urls import path
from game import views


# urls start with: account/<str:username>/team/<int:team_pk>/games/
urlpatterns = [
    path('create/', views.game_create, name='game_create'),
    # path('<int:game_pk>/starters', views.choose_starters, name='choose_starters'),
    path('<int:game_pk>/processing', views.game_processing, name='game_processing'),
    path('<int:game_pk>/players-stats', views.game_detail_players, name='game_detail_players'),
    path('<int:game_pk>/team-stats', views.game_detail_team, name='game_detail_team'),
    path('<int:game_pk>/update/', views.game_update, name='game_update'),
    path('<int:game_pk>/delete/', views.game_delete, name='game_delete')
]