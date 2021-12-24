
from django.urls import path
from account import views


urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('<str:full_name>/update/', views.update_account, name='update_account'),
    path('<str:full_name>/', views.account, name='account'),
]
