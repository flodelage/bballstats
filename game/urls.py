
from django.urls import path
from game import views


# urls start with: account/<str:username>/team/<str:team_pk>/games/
urlpatterns = [
    path('', views.games_list, name='games_list'),
]