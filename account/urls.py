
from django.urls import path
from account import views


urlpatterns = [
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('<str:full_name>/update/', views.update_account, name='update_account'),
    path('<str:full_name>/', views.account, name='account'),
]
