from django.db import models


class TimeStampedModel(models.Model):
    """[summary]
    An abstract class model that provides self
    updating ``created`` and ``modified`` fields.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
