from django.urls import path
from . import views


urlpatterns = [
    path("", views.register, name="register"),
    path("login", views.login, name="login"),
    path("<int:pk>", views.profile, name="profile"),
    path("logout", views.logout, name="logout")
]
