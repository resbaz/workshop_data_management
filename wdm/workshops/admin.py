from django.contrib import admin

from workshops.models import Person, Workshop, Participant

class PersonAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'notes']
    #list_filter = ['teaching_teams']  # cannot filter a MultiSelectField

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'start_date', 'description']

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['workshop', 'person', 'role']
    list_filter = ['person', 'workshop', 'role', 'attendance']


admin.site.register(Person, PersonAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Participant, ParticipantAdmin)