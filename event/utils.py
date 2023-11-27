# from event.models import CustomUser
from django.contrib.auth.models import User
from event.models import Conductor, Creator, Event, Participant
from django.shortcuts import get_object_or_404
from abc import ABC, abstractmethod


def validate_user(username: str, password: str) -> tuple:
    try:
        if (not username) or (not password):
            return False, "Por favor preencha todos os campos!"

        user = get_object_or_404(User, username=username)

        if not user:
            return False, "Usuário ou senha não conferem, tente novamente"

        return True, user
    except Exception:
        return False, "Usuário ou senha não conferem, tente novamente"

def check_user_fields(username: str, password: str, email: str, confirm_password: str):
    if not username or not password or not email:
        return False, "Por favor, preencha todos os campos!"

    if not (password == confirm_password):
        return False, "As senhas não coincidem!"
    
    return True, "Usuário cadastrado com sucesso!"

class ObjctFactory(ABC):
    @abstractmethod
    def criar_objeto(self):
        pass


class ParticipantFactory(ObjctFactory):
    def criar_objeto(self, username: str, password: str, email: str, confirm_password: str):

        res = check_user_fields(username, password, email, confirm_password)

        if res[0]:
            user = Participant(username=username, password=password, email=email)
            user.save()
            return res[0], res[1], user
        else:
            return res[0], res[1], None
    
class CreatorFactory(ObjctFactory):
    def criar_objeto(self, username: str, password: str, email: str):
        user = Creator(username=username, password=password, email=email)
        user.save()
        return user

class EventFactory(ObjctFactory):
    def criar_objeto(self, name: str, description: str, start_date: str, end_date: str, image: str, conductor_id: int):
        event = Event(name=name, description=description, start_date=start_date, end_date=end_date, image=image, conductor_id=conductor_id)
        event.save()
        return event
    
class ConductorFactory(ObjctFactory):
    def criar_objeto(self, username: str, password: str, email: str, confirm_password: str):

        res = check_user_fields(username, password, email, confirm_password)

        if res[0]:
            user = Conductor(username=username, password=password, email=email)
            user.save()
            return res[0], res[1], user
        else:
            return res[0], res[1], None

