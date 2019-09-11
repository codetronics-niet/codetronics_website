from django.urls import path
from .views import events, register

urlpatterns = [
    path('', events, name='tech_events'),
    path('register/', register, name='register'),
]
