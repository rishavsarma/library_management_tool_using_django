from django.urls import path
from . import views


urlpatterns = [
    path("register", views.register, name="register"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home", views.home, name="home"),
    path("", views.home, name="home"),
    path("show", views.show, name="show"),
    path('edit/logout_user', views.logout_user, name="logout_user"),
    path('edit/show', views.show, name="show"),
]