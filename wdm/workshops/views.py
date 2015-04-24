from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Workshop, Person, Institution

'''
Institution
'''

class InstitutionMixin(object):
    model = Institution

class InstitutionList(InstitutionMixin, ListView):
    pass

class InstitutionDetail(InstitutionMixin, DetailView):
    pass

class InstitutionCreate(InstitutionMixin, CreateView):
    pass


'''
Person Views
'''

class PersonMixin(object):
    model = Person

class PersonList(PersonMixin, ListView):
    pass

class PersonDetail(PersonMixin, DetailView):
    pass

class PersonCreate(PersonMixin, CreateView):
    pass

'''
Workshop Views
'''

class WorkshopMixin(object):
    model = Workshop	

class WorkshopList(WorkshopMixin, ListView):
    pass 

class WorkshopDetail(WorkshopMixin, DetailView):
    pass 

class WorkshopCreate(WorkshopMixin, CreateView):
    fields = ['title','description','start_date','teaching_hours','catering', 'website', 'blog_post']  
 
class WorkshopUpdate(WorkshopMixin, UpdateView):
    pass 

class WorkshopDelete(WorkshopMixin, DeleteView):
    pass 
