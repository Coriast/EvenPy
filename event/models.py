from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from event.manager import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# The Creator is a participant responsible for some activitiy
class Creator(CustomUser):
    pass


class Participant(CustomUser):
    pass


# The organizer is the participant who created the event and when interacting with
# chosen event he will see it from the Conductor's perspective
class Conductor(CustomUser):
    pass


class Location(models.Model):
    name = models.CharField(max_length=100)
    busy = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateTimeField()
    closed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    location = models.ForeignKey(
        Location, related_name="location", on_delete=models.CASCADE
    )
    conductor = models.ForeignKey(
        Conductor, related_name="conductor", on_delete=models.CASCADE
    )
    event = models.ForeignKey(Event, related_name="event", on_delete=models.CASCADE)
    frequency = models.TextField()

    def __str__(self) -> str:
        return self.name


class Certificate(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
