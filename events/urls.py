from django.urls import path
from .views import EventsList, EventRegisterView

urlpatterns = [
    path('', EventsList.as_view(), name='tech_events'),
    path('register/', EventRegisterView.as_view(), name='register'),
]
