from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Event, EventRegister


class EventsList(ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'


class EventRegisterView(SuccessMessageMixin, CreateView):
    model = EventRegister
    template_name = 'event_register.html'
    fields = ['title', 'student_name', 'email_id',
              'mobile_number', 'roll_no', 'branch']
