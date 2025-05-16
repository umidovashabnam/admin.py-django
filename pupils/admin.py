from django.contrib import admin
from .models import Sinf, Pupil
# Register your models here.

class AdminPupil(admin.ModelAdmin):
    search_fields = ['name','fam']
    list_filter = ['age']

admin.site.register(Sinf)
admin.site.register(Pupil,AdminPupil)