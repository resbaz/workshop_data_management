from django.db.models import Count, Min, Sum, Avg
from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

from .models import Workshop, Person, Institution, Participant, CAREER_CHOICES, DIETARY_CHOICES

''' 
Dashboard
'''

def institute_report(request, slug=""):
    institutes = Institution.objects.filter(slug__startswith=slug)
    organisation = institutes[0].organisation 
    return render(request, 'workshops/reports_institute.html', {'organisation': organisation, 'institutes': institutes}) 
     
def dashboard(request):
    ws = {}
    ws_qs = Workshop.objects.all()
    ws['ws2013_total'] = ws_qs.filter(start_date__year=2013).count()
    ws['ws2014_total'] = ws_qs.filter(start_date__year=2014).count()
    ws['ws2015_total'] = ws_qs.filter(start_date__year=2015).count()
    ws['total'] = ws['ws2013_total'] + ws['ws2014_total'] + ws['ws2015_total']    

    ws['t_hours_2013'] = 0
    for w in ws_qs.filter(start_date__year=2013):
        ws['t_hours_2013'] += w.teaching_hours    
    
    ws['t_hours_2014'] = 0
    for w in ws_qs.filter(start_date__year=2014):
        ws['t_hours_2014'] += w.teaching_hours    
    
    ws['t_hours_2015'] = 0
    for w in ws_qs.filter(start_date__year=2015):
        ws['t_hours_2015'] += w.teaching_hours    

    ws['catered'] = ws_qs.filter(catering=True).count()

    pt_qs = Participant.objects.filter(role='s')
    ppnt = {}
    total = {}
    total['all'] = 0 
    for w in ws_qs:
        if w.total_attendance() > 0:
            total['all'] += w.total_attendance()
            ppnt[w] = {}
            ppnt[w]['ws'] = w
            ppnt[w]['stats'] = w.career_stats()
            for stage_id in ppnt[w]['stats']:
                if not stage_id in total:                
                    total[stage_id] = ppnt[w]['stats'][stage_id]
                else:
                    total[stage_id] += ppnt[w]['stats'][stage_id]

    inst = []
    institutes = Institution.objects.all()
    for i in institutes:
        if i.total_attendees() > 0:
           inst.append(i) 
    attendees_per_org = Institution.counter.attendees_per_org()
    
    trainers = Person.people.return_trainers() 
    students = Person.people.return_unique_students()   
 
    return render(request, 'workshops/index.html', {'ws': ws, 'ppnt': ppnt, 'trainers':trainers, 'inst': inst, 'attendees_per_org': attendees_per_org, 'students':students, 'total':total}) 

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
