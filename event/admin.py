from django.contrib import admin
from .models import *

admin.site.register(Participant)

admin.site.register(Creator)

admin.site.register(Conductor)

admin.site.register(Location)

admin.site.register(Event)

admin.site.register(Activity)
