from django.urls import path
from . import views

urlpatterns = [
    path('', views.event, name='tech_events'),
]
