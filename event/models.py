from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from event.manager import CustomUserManager


class Participant(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(_("email address"), unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


# The Instructor is a participant responsible for some activitiy
class Instructor(Participant):
    is_instructor = models.BooleanField(default=False)


# The organizer is the participant who created the event and when interacting with
# chosen event he will see it from the Organizer's perspective
class Organizer(Participant):
    is_organizer = models.BooleanField(default=False)


class Location(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
    organizer = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateTimeField()

    def __str__(self) -> str:
        return self.name


class Activity(models.Model):
    name = models.CharField(max_length=100)
    start_hour = models.DateField()
    end_hour = models.DateField()
    location = models.ForeignKey(
        Location, related_name="location", on_delete=models.CASCADE
    )
    instructor = models.ForeignKey(
        Instructor, related_name="instructor", on_delete=models.CASCADE
    )
    event = models.ForeignKey(Event, related_name="event", on_delete=models.CASCADE)
    participants = models.ManyToManyField(
        Participant, related_name="participant", blank=True
    )

    def __str__(self) -> str:
        return self.name
