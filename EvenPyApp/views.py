from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Participant

def login(request):
    latest_login_users = Participant.objects.order_by("-username_f")
    context = { "latest_login_users": latest_login_users }
    return render(request, "EvenPyApp/login.html", context)

def register(request):
    return HttpResponse("Register screen")

def main_page(request, user_id):
    participant = get_object_or_404(Participant, pk=user_id)
    return render(request, "EvenPyApp/main_page.html", {"participant":participant})
