from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Event, EventRegister
import csv


class EventsList(ListView):
    model = Event
    template_name = 'events.html'
    context_object_name = 'events'


class EventRegisterView(CreateView):
    model = EventRegister
    template_name = 'event_register.html'
    fields = ['title', 'student_name', 'email_id',
              'mobile_number', 'roll_no', 'branch']


def export_to_csv(request):
    if (request.method == 'POST'):
        token = request.POST.get('token')
        if(token == 'NIET' or 'niet'):
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=participants.csv'
            writer = csv.writer(response)

            writer.writerow(['student_name', 'email_id',
                             'mobile_number', 'roll_no', 'branch'])
            participants = EventRegister.objects.all().values_list('student_name', 'email_id',
                                                                   'mobile_number', 'roll_no', 'branch')
            for participant in participants:
                writer.writerow(participant)
            return response
        else:
            error = "Please Enter a Valid Token"
            return render(request, 'download.html', {'error': error, })
    return render(request, 'download.html')
