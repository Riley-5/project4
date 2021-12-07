
from django.urls import path

from . import views

urlpatterns = [
    # Server paths
    path("", views.index, name="index"),
    path("following", views.following, name="following"),
    path("profile/<int:userID>", views.profile, name="profile"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API routes
    path("allPosts", views.allPosts, name="allPosts"),
]
