from event.models import CustomUser, Participant, Creator
from django.shortcuts import get_object_or_404

def validate_user(username: str, password: str) -> tuple:
    try:
        if (not username) or (not password):
            return False, "Por favor preencha todos os campos!"
        
        # para separar a View do Participante do Criador do evento
        # é necessário saber qual é qual, ao invés de puxar apenas o usuário genérico
        user = get_object_or_404(CustomUser, username=username)

        if not user:
            return False, "Usuário ou senha não conferem, tente novamente"
        
        try:
            participant = Participant.objects.get(customuser_ptr_id=user.pk)
            return True, participant
        except Participant.DoesNotExist:
            try:
                creator = Creator.objects.get(customuser_ptr_id=user.pk)
                return True, creator
            except Creator.DoesNotExist:
                return False, "Ocorreu um erro, tente novamente"

    except Exception as e:
        print(e)
        return False, "Ocorreu um erro, tente novamente"