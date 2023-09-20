from django.shortcuts import render, redirect
from django.contrib import messages, auth
from event.utils import validate_user
from event.models import Event, Conductor, Creator, Participant, CustomUser
from event.form import EventForm
from django.views import View

logged_user = None

class RegisterEventView(View):
    template_name = "event/pages/register_event.html"

    def get(self, request):
        form = EventForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        try:
            name = request.POST.get("name")
            description = request.POST.get("description")
            start_date = request.POST.get("start_date")
            end_date = request.POST.get("end_date")
            image = request.FILES.get("image")
            conductor_id = request.POST.get("conductor")

            conductor = Conductor.objects.get(id=conductor_id)

            if (
                not name
                or not description
                or not start_date
                or not end_date
                or not image
            ):
                messages.error(request, "Por favor, preencha todos os campos!")
                return redirect("register_event")

            event = Event(
                name=name,
                description=description,
                start_date=start_date,
                end_date=end_date,
                image=image,
                conductor=conductor,
            )
            event.save()
            messages.success(request, "Evento cadastrado com sucesso!")
            return redirect("home")
        except Exception as e:
            return print(e)


class EventView(View):
    template_name = "event/pages/event.html"

    def get(self, request):
        events = Event.objects.all()

        context = {"events": events}
        return render(request, self.template_name, context)


class HomeView(View):
    template_name = "event/pages/index.html"

    def get(self, request):
        global logged_user
        is_creator = isinstance(logged_user, Creator)
        return render(request, self.template_name, {"is_creator":is_creator})


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
                return redirect("login")
            
            # auth.login(request, user[1]) -> estava dando erro
            # messages.success(request, "Login efetuado com sucesso!")
            
            global logged_user
            logged_user = user[1]
            return redirect("home")
        except Exception as e:
            return print(e)


class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request, "Logout efetuado com sucesso!")
        return redirect("login")


class RegisterView(View):
    template_name = "event/pages/register.html"

    def get(self, request):
        return render(request, "event/pages/register.html")

    def post(self, request):
        try:
            type_user = request.POST.get("type_user")

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

            if type_user == "conductor":
                user = Conductor(username=username, password=password, email=email)
            elif type_user == "creator":
                user = Creator(username=username, password=password, email=email)
            else:
                user = Participant(username=username, password=password, email=email)

            user.save()
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect("login")
        except Exception as e:
            return print(e)
