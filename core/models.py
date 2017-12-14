from django.db import models

class Experiment(models.Model):
    username = models.CharField(max_length=256, blank=True, null=True)
    feedback = models.BooleanField()
    all_buttons = models.BooleanField()
    lighting_time = models.IntegerField(default=0)
    interval_time = models.IntegerField(default=0)
    session_time = models.IntegerField(default=0)

class Event(models.Model):
    experiment = models.ForeignKey('Experiment', on_delete=True)
