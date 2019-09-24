from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import redirect


class TimeStampedModel(models.Model):
    """[summary]
    An abstract class model that provides self
    updating ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Event(TimeStampedModel):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField()

    def __str__(self):
        return self.title[:50]


class EventParticipant(TimeStampedModel):
    ELECTRONICS = 'ECE'
    COMPUTER_SCIENCE = 'CSE'
    IT = 'IT'
    ELECTRICAL = 'EN'
    MECHANICAL = 'ME'
    CIVIL = 'CE'
    BIOTECH = 'BT'
    BRANCH_CHOICES = [
        (ELECTRONICS, 'Electronics'),
        (COMPUTER_SCIENCE, 'Computer Science'),
        (IT, 'IT'),
        (ELECTRICAL, 'Electrical'),
        (MECHANICAL, 'Mechanical'),
        (CIVIL, 'Civil'),
        (BIOTECH, 'Biotech'),
    ]
    title = models.ForeignKey(Event, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50, blank=True)
    email_id = models.EmailField(blank=False)
    mobile_number = models.CharField(max_length=10, blank=False)
    roll_no = models.CharField(max_length=10, blank=False)
    branch = models.CharField(
        max_length=3,
        choices=BRANCH_CHOICES,
        default=ELECTRONICS,
    )

    def __str__(self):
        return self.student_name
