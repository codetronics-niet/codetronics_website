from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin
from .models import Event, EventParticipant

admin.site.register(Event, MarkdownxModelAdmin)
admin.site.register(EventParticipant)
