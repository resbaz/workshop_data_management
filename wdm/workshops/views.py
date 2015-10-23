import csv
from collections import OrderedDict

from django.db.models import Count, Min, Sum, Avg
from django.shortcuts import render
from django.utils.text import slugify
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Workshop, Person, Institution, Participant, CAREER_CHOICES, DIETARY_CHOICES

''' 
Dashboard
'''

def institute_report(request, slug=""):
    institutes = Institution.objects.filter(slug__startswith=slug)
    organisation = institutes[0].organisation 
    return render(request, 'workshops/reports_institute.html', {'organisation': organisation, 'institutes': institutes}) 
     
def dashboard_swc(request):
    ws = {}
    ws_qs = Workshop.objects.filter(swc=True)
    ws['ws2013_total'] = ws_qs.filter(start_date__year=2013).count()
    ws['ws2014_total'] = ws_qs.filter(start_date__year=2014).count()
    ws['ws2015_total'] = ws_qs.filter(start_date__year=2015).count()
    ws['total'] = ws['ws2013_total'] + ws['ws2014_total'] + ws['ws2015_total']    
    
    swc_participants = 0
    for workshop in ws_qs.filter(start_date__year=2013):
        swc_participants += workshop.total_attendance()
    ws['swc_participants_2013'] = swc_participants
    
    swc_participants = 0
    for workshop in ws_qs.filter(start_date__year=2014):
        swc_participants += workshop.total_attendance()
    ws['swc_participants_2014'] = swc_participants
    
    swc_participants = 0
    for workshop in ws_qs.filter(start_date__year=2015):
        swc_participants += workshop.total_attendance()
    ws['swc_participants_2015'] = swc_participants
    
    swc_participants = 0
    for workshop in ws_qs.filter(swc=True):
        swc_participants += workshop.total_attendance()
    ws['swc_participants'] = swc_participants

    ppnt = {}
    total = {}
    total['all'] = 0 
    for w in ws_qs:
        if w.total_attendance() > 0:
            total['all'] += w.total_attendance()
            ppnt[w.slug] = {}
            ppnt[w.slug]['ws'] = w
            ppnt[w.slug]['stats'] = w.career_stats()
            for stage_id in ppnt[w.slug]['stats']:
                if not stage_id in total:                
                    total[stage_id] = ppnt[w.slug]['stats'][stage_id]
                else:
                    total[stage_id] += ppnt[w.slug]['stats'][stage_id]
            ppnt[w.slug]['m'] = w.get_male_student_count()
            ppnt[w.slug]['f'] = w.get_female_student_count()
            ppnt[w.slug]['u'] = w.get_unknown_gender_student_count()
    sorted_ppnt = OrderedDict(sorted(ppnt.items(), key=lambda t: t[0], reverse=True))    

    attendees_per_org = Institution.counter.attendees_swc_per_org()
    sorted_attendees = OrderedDict(sorted(attendees_per_org.items(), key=lambda(k,v): v.values(), reverse=True))
    trainers = Person.people.return_swc_trainers() 
    students = Person.people.return_unique_swc_students()   
 
    return render(request, 'workshops/swc_dash.html', {'ws': ws, 'ppnt': sorted_ppnt, 'trainers':trainers, 'students':students, 'attendees_per_org': sorted_attendees, 'total':total}) 

def dashboard(request):
    ws = {}
    ws_qs = Workshop.objects.all()
    ws['ws2013_total'] = ws_qs.filter(start_date__year=2013).count()
    ws['ws2014_total'] = ws_qs.filter(start_date__year=2014).count()
    ws['ws2015_total'] = ws_qs.filter(start_date__year=2015).count()
    ws['total'] = ws['ws2013_total'] + ws['ws2014_total'] + ws['ws2015_total']    

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
    sorted_ppnt = OrderedDict(sorted(ppnt.items(), key=lambda t: t[0], reverse=True))    


    attendees_per_org = Institution.counter.attendees_per_org()
    sorted_attendees = OrderedDict(sorted(attendees_per_org.items(), key=lambda(k,v): v.values(), reverse=True))
    
    trainers = Person.people.return_trainers() 
    students = Person.people.return_unique_students()   
 
    return render(request, 'workshops/index.html', {'ws': ws, 'ppnt': sorted_ppnt, 'trainers':trainers, 'attendees_per_org': sorted_attendees, 'students':students, 'total':total}) 

def dashboard_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="dashboard.csv"'
    
    writer = csv.writer(response)

    '''
    Stats about Workshops
    '''

    ws = {}
    ws_qs = Workshop.objects.all()
    ws['ws2013_total'] = ws_qs.filter(start_date__year=2013).count()
    ws['ws2014_total'] = ws_qs.filter(start_date__year=2014).count()
    ws['ws2015_total'] = ws_qs.filter(start_date__year=2015).count()
    ws['total'] = ws['ws2013_total'] + ws['ws2014_total'] + ws['ws2015_total']    

    writer.writerow(['Workshops'])
    writer.writerow(['total WS', '2013', '2014', '2015'])
    writer.writerow([ws['total'], ws['ws2013_total'], ws['ws2014_total'], ws['ws2015_total']])
    writer.writerow([''])

    ws['t_hours_2013'] = 0
    for w in ws_qs.filter(start_date__year=2013):
        ws['t_hours_2013'] += w.teaching_hours    
    
    ws['t_hours_2014'] = 0
    for w in ws_qs.filter(start_date__year=2014):
        ws['t_hours_2014'] += w.teaching_hours    
    
    ws['t_hours_2015'] = 0
    for w in ws_qs.filter(start_date__year=2015):
        ws['t_hours_2015'] += w.teaching_hours    

    writer.writerow(['WS teaching hours', '2013', '2014', '2015'])
    writer.writerow(['', ws['t_hours_2013'], ws['t_hours_2014'], ws['t_hours_2015']])
    writer.writerow([''])

    ws['swc'] = ws_qs.filter(swc=True).count()

    swc_participants = 0
    for workshop in ws_qs.filter(swc=True).filter(start_date__year=2015):
        swc_participants += workshop.total_attendance()
    ws['swc_participants_2015'] = swc_participants
    
    swc_participants = 0
    for workshop in ws_qs.filter(swc=True):
        swc_participants += workshop.total_attendance()
    ws['swc_participants'] = swc_participants

    writer.writerow(['Software Carpentry Workshops', '2013', '2014', '2015', 'total'])
    writer.writerow(['# held', '1', '6', ws_qs.filter(swc=True).filter(start_date__year=2015).count(), ws['swc']])
    writer.writerow(['students attended', '44', '212', ws['swc_participants_2015'], ws['swc_participants']])
    writer.writerow([''])
    
    '''
    Stats about Participants
    '''
    writer.writerow(['Participants'])

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
    
    phd_total = total['4'] + total['5'] + total['6']
    writer.writerow(["Participant's Career stage", 'UG', 'Honours', 'Masters', 'PhD', 'Postgraduate', 'Post Doc', 'ECR', 'MCR', 'Senior Researcher', 'RA', 'Professional'])
    writer.writerow(['', total['1'], total['2'], total['3'], phd_total, total['7'], total['8'], total['9'],total['10'], total['11'], total['12'], total['13']])
    writer.writerow([''])


    '''
    Stats about institutions
    '''

    attendees_per_org = Institution.counter.attendees_per_org()

    list_inst = []
    list_count = []
    for inst_name, slug_count in attendees_per_org.iteritems():
        list_inst.append(inst_name)
        list_count.append(slug_count.values()[0])
    writer.writerow(['Institutions'])
    writer.writerow(list_inst)
    writer.writerow(list_count)
    writer.writerow([''])
    
    '''
        Stats about humans
    '''

    trainers = Person.people.return_trainers() 
    students = Person.people.return_unique_students()   
    
    writer.writerow(['People'])
    writer.writerow(['total students', 'Male', 'Female', 'Other', 'Unknown'])
    unknown_gender = students['u'] + students[''] 
    writer.writerow([students['total'], students['m'], students['f'], students['o'], unknown_gender])
    writer.writerow([''])
    writer.writerow(['total Trainers', 'Instructors', 'Helpers'])
    writer.writerow([trainers['total'], trainers['i'], trainers['h']])
 
    return response


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
    fields = ['title','description','start_date','teaching_hours','catering', 'website', 'blog_post', 'swc']  
 
class WorkshopUpdate(WorkshopMixin, UpdateView):
    pass 

class WorkshopDelete(WorkshopMixin, DeleteView):
    pass 
