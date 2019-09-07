from django.db import models
from django.urls import reverse_lazy


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
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title[:50]


class EventRegister(TimeStampedModel):
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
    student_name = models.CharField(max_length=50)
    email_id = models.EmailField()
    mobile_number = models.IntegerField()
    roll_no = models.IntegerField()
    branch = models.CharField(
        max_length=3,
        choices=BRANCH_CHOICES,
        default=ELECTRONICS,
    )

    def __str__(self):
        return self.student_name

    def get_absolute_url(self):
        return reverse_lazy("homepage")
