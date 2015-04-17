from django.contrib import admin
#from import_export import resources
#from import_export.admin import ImportExportActionModelAdmin

from workshops.models import Person, Workshop, Participant, Institution

#class WorkshopResource(resources.ModelResource):
    
#    class Meta:
#        model Workshop


class PersonAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'notes']
    list_filter = ['teaching_team']

class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'start_date', 'description']
    #resource_class = WorkshopResource    

class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['workshop', 'person', 'role']
    list_filter = ['person', 'workshop', 'role', 'attendance_start', 'attendance_end']
    fieldsets = (
        (None, {'fields': ('workshop',)}),
        ('Participant', {'fields':('person', 'institution', 'role', 'career_stage',)}),
        ('Dietary requirements', {'fields': ('vegan', 'vegetarian', 'gluten_free', 'lactose_intolerant', 'other_diet'), 'classes': ('collapse',),}),
        ('Attendance', {'fields': ('offer', 'acceptance', 'attendance_start', 'attendance_end')}),
        )

class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['__unicode__']
    list_filter = ['organisation', 'campus', 'department']

admin.site.register(Person, PersonAdmin)
admin.site.register(Workshop, WorkshopAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Institution, InstitutionAdmin)

