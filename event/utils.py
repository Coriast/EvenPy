from event.models import Organizer 
from django.shortcuts import get_object_or_404

def validate_user(username: str, password: str) -> tuple:
    try:
        if (not username) or (not password):
            return False, "Por favor preencha todos os campos!"
        
        user = get_object_or_404(Organizer, username=username) 

        if not user:
            return False, "Usuário ou senha não conferem, tente novamente"
        
        return True, user
    except Exception:
        return False, "Usuário ou senha não conferem, tente novamente"