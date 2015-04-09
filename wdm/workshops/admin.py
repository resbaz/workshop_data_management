from django.contrib import admin

from workshops.models import Person, Workshop, Participant, Institution

class PersonAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'notes']
    list_filter = ['teaching_team']

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'start_date', 'description']

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['workshop', 'person', 'role']
    list_filter = ['person', 'workshop', 'role', 'attendance']

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['__unicode__']
    list_filter = ['organisation', 'campus', 'department']


admin.site.register(Person, PersonAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Institution, InstitutionAdmin)