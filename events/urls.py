from django.urls import path

from .views import events
from .views import register
from .views import request_event

urlpatterns = [
    path("", events, name="tech_events"),
    path("register/", register, name="register"),
    path("request_event/", request_event, name="request_event"),
]
