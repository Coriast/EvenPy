from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("index/", views.HomeView.as_view(), name="home"),
    path("event/", views.EventView.as_view(), name="event"),
]