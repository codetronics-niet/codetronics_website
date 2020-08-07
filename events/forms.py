from django.forms import ModelForm

from .models import EventParticipant, RequestEvent


class ParticipantForm(ModelForm):
    class Meta:
        model = EventParticipant
        fields = [
            "title",
            "student_name",
            "email_id",
            "mobile_number",
            "roll_no",
            "branch",
        ]


class RequestEventForm(ModelForm):
    class Meta:
        model = RequestEvent
        fields = ["title", "description", "your_name", "roll_no", "contact"]
