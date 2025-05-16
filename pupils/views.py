from django.http import HttpResponse
from .models import Pupil, Sinf
from django.shortcuts import render

# Create your views here.
def salom(request):
    return HttpResponse("Salom")

def info(request, sinf, name):
    pupil = Pupil.objects.get(name = name)
    return HttpResponse(f" {pupil.fam} {pupil.name}  {pupil.age }")



    # pupil = Pupil.objects.get(name=name)
    # return HttpResponse(f"{pupil.fam} {pupil.name} {pupil.age} yosh")