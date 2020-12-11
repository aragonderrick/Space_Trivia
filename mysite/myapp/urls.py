from django.urls import path
from django.contrib.auth import views as auth_views

from . import views #convention

urlpatterns = [
    path('', views.compete),
    path('login/', auth_views.LoginView.as_view()),
    path('register/', views.register),
    path('logout/', views.logout_view),
    path('suggestions/', views.get_suggestions),
    path('compete/', views.compete),
    path('leaderboard/', views.leaderboard),
    path('game/', views.game),
    path('chat/', views.chat),
    path('contact/', views.contact, name="contact"),
    path('setscore/<int:s>', views.scoreSet)
]