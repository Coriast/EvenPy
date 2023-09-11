from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Participant

def login(request):
    latest_login_users = Participant.objects.order_by("-username_f")
    context = { "latest_login_users": latest_login_users }
    return render(request, "EvenPyApp/pages/login.html", context)

def register(request):
    return render(request, "EvenPyApp/pages/register.html")


def index(request):
    return render(request, "EvenPyApp/pages/index.html")


def main_page(request, user_id):
    participant = get_object_or_404(Participant, pk=user_id)
    return render(request, "EvenPyApp/pages/main_page.html", {"participant":participant})
