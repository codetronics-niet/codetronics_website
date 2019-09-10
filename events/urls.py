from django.urls import path
from .views import EventsList, register

urlpatterns = [
    path('', EventsList.as_view(), name='tech_events'),
    path('register/', register, name='register'),
]
