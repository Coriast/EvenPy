from django.db import models
from datetime import date

# All users who have a login
class AbstractUser(models.Model):
    username    = models.CharField(max_length=100)
    email       = models.CharField(max_length=100)
    password    = models.CharField(max_length=20)

# When joined in an event the user becomes a participant in that event
class Participant(AbstractUser):
    def __str__(self):
        return self.username

# The Instructor is a participant responsible for some activitiy
class Instructor(Participant):
    pass

# The organizer is the participant who created the event and when interacting with 
# chosen event he will see it from the Organizer's perspective
class Organizer(Participant):
    pass

class Location(models.Model):
    name = models.CharField(max_length=100)

class Event(models.Model):
    name        = models.CharField(max_length=100)
    organizer   = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()

class Activity(models.Model):
    name            = models.CharField(max_length=100)
    start_hour      = models.DateTimeField()
    end_hour        = models.DateTimeField()
    location        = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    instructor      = models.ForeignKey(Instructor, related_name='instructor', on_delete=models.CASCADE)
    event           = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)
    participants    = models.ManyToManyField(Participant, related_name='participant', blank=True)
