"""bballstats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from account import views as account_views


urlpatterns = [
    path('', account_views.home, name='home'),

    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('account/<str:username>/teams/', include('team.urls')),
    path('account/<str:username>/team/<int:team_pk>/players/', include('player.urls')),
    path('account/<str:username>/team/<int:team_pk>/games/', include('game.urls')),
    path('account/<str:username>/team/<int:team_pk>/', include('statistic.urls')),
]
