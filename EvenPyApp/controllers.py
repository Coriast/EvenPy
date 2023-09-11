from .models import User, Participant, Organizer, Instructor

class LoginManager:
    user_f: User

    def __init__(self, user):
        self.user_f = user

    def check_login():
        user_exists = User.objects.get( email_f__iexact = user_f.email_f )
        if user_exists == None:
            print("test")
        else:
            print(user_exists.username_f)

