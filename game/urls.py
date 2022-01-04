
from django.urls import path
from game import views


# urls start with: account/<str:username>/team/<int:team_pk>/games/
urlpatterns = [
    path('', views.games_list, name='games_list'),
    path('<int:game_pk>/', views.game_detail, name='game_detail'),
]