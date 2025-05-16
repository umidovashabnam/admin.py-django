from tkinter.constants import CASCADE

from django .db import models
from django.db.models import CharField


class Sinf(models.Model):
    name = models.CharField(max_length=20)
    max_pupils = models.IntegerField()

    def __str__(self):
      return self.name

class Pupil(models.Model):
    name = models.CharField(max_length=20)
    fam = models.CharField(max_length=20)
    age = models.IntegerField()
    sinf = models.ForeignKey(Sinf, on_delete = models.CASCADE)

    def __str__(self):
      return f"{self.fam} - {self.name}"