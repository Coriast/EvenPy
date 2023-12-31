from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Creator(User):
    class Meta:
        verbose_name = _("creator")
        verbose_name_plural = _("creators")


class Participant(User):
    class Meta:
        verbose_name = _("participant")
        verbose_name_plural = _("participants")


class Conductor(User):
    events = models.ManyToManyField("Event", related_name="events")

    class Meta:
        verbose_name = _("conductor")
        verbose_name_plural = _("conductors")


class Location(models.Model):
    name = models.CharField(max_length=100)
    busy = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="images/")
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
