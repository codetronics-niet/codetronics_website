from django.forms import ModelForm
from .models import EventParticipant, requestEvent


class ParticipantForm(ModelForm):
    class Meta:
        model = EventParticipant
        fields = ['title', 'student_name',
                  'email_id', 'mobile_number', 'roll_no', 'branch']

class requestEventForm(ModelForm):
    class Meta:
        model = requestEvent
        fields = ['title', 'description', 'your_name','roll_no' ,'contact']
