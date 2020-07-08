from django.contrib import admin
from .models import Event, EventParticipant, requestEvent

admin.site.register(Event)
admin.site.register(EventParticipant)
admin.site.register(requestEvent)
