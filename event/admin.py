from django.contrib import admin
from .models import *

admin.site.register(Participant)

admin.site.register(Instructor)

admin.site.register(Organizer)

admin.site.register(Location)

admin.site.register(Event)

admin.site.register(Activity)
