from django.forms import ModelForm
from .models import EventParticipant


class ParticipantForm(ModelForm):
    class Meta:
        model = EventParticipant
        fields = ['title', 'student_name',
                  'email_id', 'mobile_number', 'roll_no', 'branch']
