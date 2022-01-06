
from django.urls import path
from team import views


# urls start with: account/<str:username>/teams/
urlpatterns = [
    path('create/', views.team_create, name='team_create'),
    path('', views.teams_list, name='teams_list'),
    path('<int:team_pk>/', views.team_detail, name='team_detail'),
    path('<int:team_pk>/update/', views.team_update, name='team_update'),
    path('<int:team_pk>/delete/', views.team_delete, name='team_delete'),
    path('select/', views.team_select, name='team_select')
]