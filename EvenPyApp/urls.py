from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("<int:user_id>/", views.main_page, name="main")
]