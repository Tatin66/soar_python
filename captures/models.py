from django.db import models

# Create your models here.

#creation du model et de la base de doneé corréspondante
class Captures(models.Model):
    interface = models.CharField(max_length=255)
    nb_packet = models.IntegerField()
    date_heure = models.DateTimeField()
    fait = models.BooleanField(default=False)