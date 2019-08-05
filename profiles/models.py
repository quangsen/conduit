from django.db import models
from core.models import TimestampedModel

class Profile(TimestampedModel):
    bio = models.TextField(blank=True)