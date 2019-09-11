from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Event, EventParticipant
from .forms import ParticipantForm
import csv


def events(request):
    events = Event.objects.all
    return render(request, 'events.html', {'events': events})


def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('student_name')
            messages.success(
                request, f'Thank you {name} for registering yourself, you will be contacted shortly')
            return redirect('homepage')
    else:
        form = ParticipantForm()
    return render(request, 'event_register.html', {'form': form})


def export_to_csv(request):
    if (request.method == 'POST'):
        token = request.POST.get('token')
        if token == 'niet':
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename=participants.csv'
            writer = csv.writer(response)

            writer.writerow(['student_name', 'email_id',
                             'mobile_number', 'roll_no', 'branch'])
            participants = EventParticipant.objects.all().values_list('student_name', 'email_id',
                                                                      'mobile_number', 'roll_no', 'branch')
            for participant in participants:
                writer.writerow(participant)
            return response
        else:
            error = "Please Enter a Valid Token"
            return render(request, 'download.html', {'error': error})
    return render(request, 'download.html')
