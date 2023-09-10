from django.db import models
from datetime import date

class BasicModel(models.Model):
    name_f = models.CharField(max_length=100)
    def __str__(self):
        return self.name_f

# All users who have a login
class AbstractUser(BasicModel):
    username_f    = models.CharField(max_length=100)
    email_f       = models.CharField(max_length=100)
    password_f    = models.CharField(max_length=20)
    def __str__(self):
        return self.username_f

# When joined in an event the user becomes a participant in that event
class Participant(AbstractUser):
    pass

# The Instructor is a participant responsible for some activitiy
class Instructor(Participant):
    pass

# The organizer is the participant who created the event and when interacting with 
# chosen event he will see it from the Organizer's perspective
class Organizer(Participant):
    pass

class Location(BasicModel):
    pass

class Event(BasicModel):
    organizer_f   = models.ForeignKey(Organizer, on_delete=models.CASCADE)
    start_date_f  = models.DateTimeField()
    end_date_f    = models.DateTimeField()

class Activity(BasicModel):
    start_hour_f      = models.DateTimeField()
    end_hour_f        = models.DateTimeField()
    location_f        = models.ForeignKey(Location, related_name='location', on_delete=models.CASCADE)
    instructor_f      = models.ForeignKey(Instructor, related_name='instructor', on_delete=models.CASCADE)
    event_f           = models.ForeignKey(Event, related_name='event', on_delete=models.CASCADE)
    participants_f    = models.ManyToManyField(Participant, related_name='participant', blank=True)
