from django.contrib import admin

from .models import Event
from .models import EventParticipant
from .models import RequestEvent

admin.site.register(Event)
admin.site.register(EventParticipant)
admin.site.register(RequestEvent)
