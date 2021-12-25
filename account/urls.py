
from django.urls import path
from account import views


urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('<str:username>/update/', views.update_account, name='update_account'),
    path('<str:username>/', views.account, name='account'),
]
