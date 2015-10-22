from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
from workshops.models import Person, Workshop, Institution, Participant


# Resources for import/export functionality

class PersonResource(resources.ModelResource):
    
    class Meta:
        model = Person

class WorkshopResource(resources.ModelResource):

    class Meta:
        model = Workshop 

class InstitutionResource(resources.ModelResource):

    class Meta:
        model = Institution

class ParticipantResource(resources.ModelResource):
    
    class Meta:
        model = Participant

# Admin site specifications

class WorkshopAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'title', 'start_date', 'description', 'swc', 'total_attendance']
    resource_class = WorkshopResource

class InstitutionAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'organisation', 'department', 'campus', 'total_attendees']
    list_filter = ['organisation',]
    resource_class = InstitutionResource

class ParticipantInline(admin.TabularInline):
    model = Participant

class PersonAdmin(ImportExportActionModelAdmin):
    inlines = [ParticipantInline, ]
    list_display = ['id', 'name', 'notes']
    list_filter = ['teaching_team']
    resource_class = PersonResource
    search_fields = ['name', 'email']

class ParticipantAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'workshop', 'person', 'role']
    list_filter = ['role', 'attendance_start', 'attendance_end', 'workshop', 'institution']
    raw_id_fields = ('person', 'workshop',) 
    fieldsets = (
        (None, {'fields': ('workshop',)}),
        ('Participant', {'fields':('person', 'institution', 'role', 'career_stage',)}),
        ('Dietary requirements', {'fields': ('vegan', 'vegetarian', 'gluten_free', 'lactose_intolerant', 'other_diet'), 'classes': ('collapse',),}),
        ('Attendance', {'fields': ('offer', 'acceptance', 'attendance_start', 'attendance_end')}),
        )
    resource_class = ParticipantResource


admin.site.register(Person, PersonAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Institution, InstitutionAdmin)
