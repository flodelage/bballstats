
from django.urls import path
from player import views


# urls start with: account/<str:username>/team/<str:team_pk>/players/
urlpatterns = [
    path('', views.players_list, name='players_list'),
]
