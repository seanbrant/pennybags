from django.conf import settings
from django.db import models


class Prize(models.Model):
    id = models.CharField(max_length=1, primary_key=True)
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Marker(models.Model):
    id = models.IntegerField(primary_key=True)
    prize = models.ForeignKey(Prize)


class CollectedMarker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    marker = models.ForeignKey(Marker)
