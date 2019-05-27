from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('vote/', views.vote, name='vote'),
    path('login/', auth_views.LoginView.as_view(template_name="elections_beta/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name="elections_beta/logout.html"), name="logout"),
    path('count/', views.count, name='count'),
]
