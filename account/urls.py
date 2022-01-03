
from django.urls import path
from account import views


urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('<str:username>/', views.account, name='account'),
    path('<str:username>/update-informations/', views.update_informations, name='update_informations'),
    path('<str:username>/update-password/', views.update_password, name='update_password'),
    path('<str:username>/delete/', views.account_delete, name='account_delete'),
]
