from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("index/", views.HomeView.as_view(), name="home"),
    path("event/", views.EventView.as_view(), name="events"),
    path("event/<int:pk>/", views.EventDetailView.as_view(), name="event_detail"),
    path("add-event/", views.RegisterEventView.as_view(), name="register_event"),
    path("add-conductor/", views.RegisterConductorView.as_view(), name="register_conductor"),
]