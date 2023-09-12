from django.shortcuts import render, redirect
from django.contrib import messages, auth
from event.utils import validate_user
from .models import Participant
from django.views import View


class HomeView(View):
    template_name = "event/pages/index.html"

    def get(self, request):
        return render(request, self.template_name)


class LoginView(View):
    template_name = "event/pages/login.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = validate_user(username=username, password=password)

            if not user[0]:
                messages.error(request, user[1])
                return redirect('login')

            messages.success(request, "Login efetuado com sucesso!")
            return redirect("home")
        except Exception as e:
            return print(e)

class LogoutView(View):
    def post(self, request):
        messages.success(request, "Logout efetuado com sucesso!")
        return redirect("login")

class RegisterView(View):
    template_name = "event/pages/register.html"

    def get(self, request):
        return render(request, "event/pages/register.html")

    def post(self, request):
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            confirm_password = request.POST.get("confirm_password")
            email = request.POST.get("email")

            if not username or not password or not email:
                messages.error(request, "Por favor, preencha todos os campos!")
                return redirect("register")

            if not (password == confirm_password):
                messages.error(request, "As senhas não coincidem!")
                return redirect("register")

            participant = Participant(username=username, password=password, email=email)
            participant.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect("login")
        except Exception as e:
            return print(e)