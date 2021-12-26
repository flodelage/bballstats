
from django.urls import path
from statistic import views


# urls start with: account/<str:username>/team/<str:team_pk>/
urlpatterns = [
    path('averages/', views.averages, name='averages'),
]