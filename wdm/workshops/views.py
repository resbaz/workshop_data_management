from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Workshop

'''
Workshop Views
'''

class WorkshopList(ListView):
    model = Workshop

class WorkshopDetail(DetailView):
    model = Workshop

class WorkshopCreate(CreateView):
    model = Workshop
    fields = ['title','description','start_date','teaching_hours','catering']  
 
class WorkshopUpdate(UpdateView):
    model = Workshop

class WorkshopDelete(DeleteView):
    model = Workshop
