from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from workshops.models import Person, Workshop, Participant, Institution


class WorkshopResource(resources.ModelResource):

    class Meta:
        model = Workshop 

class InstitutionResource(resources.ModelResource):

    class Meta:
        model = Institution

class PersonResource(resources.ModelResource):
    
    class Meta:
        model = Person

class ParticipantResource(resources.ModelResource):
    
    class Meta:
        model = Participant

class PersonAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'notes']
    list_filter = ['teaching_team']
    resource_class = PersonResource

class WorkshopAdmin(ImportExportActionModelAdmin):
    list_display = ['id', '__unicode__', 'start_date', 'description']
    resource_class = WorkshopResource

class ParticipantAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'workshop', 'person', 'role']
    list_filter = ['person', 'workshop', 'role', 'attendance_start', 'attendance_end']
    fieldsets = (
        (None, {'fields': ('workshop',)}),
        ('Participant', {'fields':('person', 'institution', 'role', 'career_stage',)}),
        ('Dietary requirements', {'fields': ('vegan', 'vegetarian', 'gluten_free', 'lactose_intolerant', 'other_diet'), 'classes': ('collapse',),}),
        ('Attendance', {'fields': ('offer', 'acceptance', 'attendance_start', 'attendance_end')}),
        )
    resource_class = ParticipantResource

class InstitutionAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'organisation', 'campus', 'department']
    list_filter = ['organisation', 'campus', 'department']
    resource_class = InstitutionResource

admin.site.register(Person, PersonAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Institution, InstitutionAdmin)

