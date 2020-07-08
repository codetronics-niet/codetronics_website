from django.urls import path
from .views import events, register, requestEvent

urlpatterns = [
    path('', events, name='tech_events'),
    path('register/', register, name='register'),
    path('requestEvent/', requestEvent, name='requestEvent'),
]
