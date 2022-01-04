
from django.urls import path
from game import views


# urls start with: account/<str:username>/team/<int:team_pk>/games/
urlpatterns = [
    path('<int:game_pk>/', views.game_detail, name='game_detail'),
    path('<int:game_pk>/update/', views.game_update, name='game_update'),
    path('<int:game_pk>/delete/', views.game_delete, name='game_delete')
]