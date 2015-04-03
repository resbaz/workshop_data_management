from django.contrib import admin

from workshops.models import Person, Workshop, Participant

admin.site.register(Person)
admin.site.register(Workshop)
admin.site.register(Participant)