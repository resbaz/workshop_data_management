from django.contrib import admin

from workshops.models import Applicant, Helper, Instructor, Organisation, Person, Student, Workshop

admin.site.register(Applicant)
admin.site.register(Helper)
admin.site.register(Instructor)
admin.site.register(Organisation)
admin.site.register(Person)
admin.site.register(Student)
admin.site.register(Workshop)