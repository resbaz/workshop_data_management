""" models.py
    contains the models for:
    
"""

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify

from autoslug import AutoSlugField
from collections import defaultdict

GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Other'),
    ('u', 'Unknown'),
    ('t', 'TEMP'),
    )

ROLE_CHOICES = (
    ('i', 'Instructor'),
    ('h', 'Helper'),
    ('s', 'Student'),
    ('t', 'TEMP'),
    )

TEACHING_TEAM_CHOICES = (
    ('p', 'Python'),
    ('r', 'R'),
    ('m', 'MATLAB'),
    ('n', 'NLTK'),
    )

CAREER_CHOICES = (
    ('1', 'Undergraduate'),
    ('2', 'Honours'),
    ('3', 'Masters'),
    ('4', 'PhD - first year'),
    ('5', 'PhD - second year'),
    ('6', 'PhD - third year and beyond'),
    ('7', 'Postgraduate student'),
    ('8', 'Postdoc'),
    ('9', 'Early career researcher'),
    ('10', 'Mid career researcher'),
    ('11', 'Senior researcher'),
    ('12', 'Research assistant'),
    ('13', 'Professional'),
    )

DIETARY_CHOICES = (
    ('1', 'Vegetarian'),
    ('2', 'Vegan'),
    ('3', 'Gluten free'),
    ('5', 'Lactose intolerant'),
    ('6', 'Halal'),
    ('7', 'Kosher'),
    )


class PersonManager(models.Manager):
    """ Table level functions for people"""
    def return_unique_students(self):
        ppl = Person.objects.all()
        student_count = defaultdict(int)
        for p in ppl:
            student = p.participations.filter(role='s')
            if len(student)>0:
                student_count['total'] += 1
                student_count[p.gender] += 1
        return student_count
    
    def return_trainers(self):
        ppl = Person.objects.all()
        trainer_count = defaultdict(int)
        for p in ppl:
            trainings = p.participations.exclude(role='s')
            helper=False
            instructor=False
            if len(trainings)>0:
                trainer_count['total'] += 1
                for trainer in trainings:
                    if not helper and trainer.role=='h':
                        trainer_count[trainer.role] += 1
                        helper=True
                    if not instructor and trainer.role=='i':
                        trainer_count[trainer.role] += 1
                        instructor=True
        return trainer_count
        

class Person(models.Model):
    """The underlying model for a person."""

    name = models.CharField(max_length=128)
    email = models.EmailField()
    mobile = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, blank=True)
    dob = models.DateField(u'Date of Birth', blank=True, null=True)

    notes = models.CharField(max_length=200, blank=True)

    teaching_team = models.CharField(max_length=10, choices=TEACHING_TEAM_CHOICES, blank=True)     
    email_list = models.BooleanField(u'Happy to be on email list', default=True)         

    slug = AutoSlugField(populate_from='name', unique=True, always_update=True)
    
    objects = models.Manager()
    people = PersonManager()

    def __unicode__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return reverse('person_detail', args=[self.slug])
        
    def first_letter(self):
        first, last = self.name.split(' ',1)
        return last[0].upper() or ''
    
    def workshops_attended(self):
        ws = []
        for participations in self.participations.all():
            ws.append(participations.workshop)
        return ws

    def participations(self):
        return self.participations.all()
    
    def institutions(self):
        institutions = []
        for ws in self.workshops_attended():
            institutions.append(ws.institution)
    
    class Meta:
        ordering = ['name', ]
        unique_together = ('name', 'email')
        verbose_name_plural = "People"    

class Workshop(models.Model):
    """Underlying model for workshops."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True)
    start_date = models.DateField()
    teaching_hours = models.FloatField()
    catering = models.BooleanField(default=False)
    
    swc = models.NullBooleanField('SWC') 
 
    website = models.URLField(blank=True)
    blog_post = models.URLField(blank=True)
   
    slug = models.SlugField(max_length=115, blank=True)   
 
    def __unicode__(self):
        return '%s: %s' % (self.start_date, self.title)
    
    def get_absolute_url(self):
        return reverse('workshop_detail', args=[self.slug])

    def total_attendance(self):
        return self.participants.filter(role='s').count()
   
    def students(self):
        return self.participants.all()    

    def institute_stats(self):
        inst_stats = {}
        for participant in self.participants.all():
            if participant.institution not in inst_stats: 
                inst_stats[participant.institution] = 1
            else:
                inst_stats[participant.institution] += 1
        return inst_stats

    def career_stats(self):
        career_stats = {}
        for stage_id, stage in CAREER_CHOICES:
            career_stats[stage_id]=self.participants.filter(career_stage=stage_id).count()
        return career_stats

    def save(self):
        """This creates the slug automagically from the date and title"""
        if not self.slug:
            temp = "%s %s" %(self.start_date, self.title)
            self.slug = slugify(temp)
        super(Workshop, self).save()    

    class Meta:
        ordering = ['-start_date',]


class ArtsManager(models.Manager):
    def with_counts(self):
        total = 0
        
        uom = Institution.objects.filter(organisation="University of Melbourne")
        for org in uom:
            if org.department in arts_orgs:
                total += org.total_attendees()
        return total
                  
    def get_queryset(self):
        artsOrgs = ["Faculty of Arts", "School of Social and Political Sciences", "School of Languages and Linguistics", "School of Historical and Philosophical Studies", "School of Culture and Communication", "Graduate School of Humanities and Social Sciences", "Asia Institute", ]
        return super(ArtsManager, self).get_queryset().filter(organisation="University of Melbourne", department__in=artsOrgs)


class InstitutionManager(models.Manager):
    def attendees_per_org(self):
        total = {}
        for org in Institution.objects.distinct('organisation').values('organisation'):
            if Participant.objects.filter(institution__organisation=org['organisation']).count()>0:
                org_slug = slugify(org['organisation'])
                total[org['organisation']] = {org_slug: Participant.objects.filter(institution__organisation=org['organisation']).count()}
        return total

class Institution(models.Model):
    """Underlying model for institutions."""
    
    organisation = models.CharField(max_length=100)
    campus = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=200, blank=True)

    objects = models.Manager() 
    counter = InstitutionManager()
    artsmanager = ArtsManager()

    def __unicode__(self):
        temp_name = self.organisation
        if self.campus:
            temp_name += " (%s)" % self.campus
        if self.department:
            temp_name += ", %s" % self.department
        return temp_name 

    def get_absolute_url(self):
        return reverse('institution_detail', args=[self.slug])

    def total_attendees(self):
        return Participant.objects.filter(institution=self).count()
        
    def male_attendees(self):
        return Participant.objects.filter(institution=self, person__gender='m').count()
        
    def female_attendees(self):
        return Participant.objects.filter(institution=self, person__gender='f').count()
    
    def other_attendees(self):
        return Participant.objects.filter(institution=self, person__gender='o').count()
        
    def unknown_attendees(self):
        return self.total_attendees() - self.male_attendees() - self.female_attendees() - self.other_attendees()
    
    '''
    def org_stats(self):
        org_slug = slugify(self.organisation)
        return "/reports/%s/" % org_slug 
    '''
    def save(self):
        if not self.slug:
             self.slug = slugify(self)
        super(Institution, self).save()

    class Meta:
        ordering = ['organisation', 'department']
    

class Participant(models.Model):
    """Intermediate class for workshop participants."""

    person = models.ForeignKey(Person, related_name='participations')
    workshop = models.ForeignKey(Workshop, related_name='participants')
    institution = models.ForeignKey(Institution, related_name='participants')

    role = models.CharField(max_length=2, choices=ROLE_CHOICES)
    career_stage = models.CharField(u'career stage', max_length=4, choices=CAREER_CHOICES, blank=True)
    
    offer = models.BooleanField(u'offered a ticket', default=False)   
    acceptance = models.BooleanField(u'accepted a ticket', default=False)   
    attendance_start = models.NullBooleanField(u'attended the beginning of the workshop', default=None)   
    attendance_end = models.NullBooleanField(u'was still there at the end of the workshop', default=None)

    vegan = models.NullBooleanField(default=None)
    vegetarian = models.NullBooleanField(default=None)
    gluten_free = models.NullBooleanField(default=None)
    lactose_intolerant = models.NullBooleanField(default=None)
    other_diet = models.CharField(u'other dietary requirements', max_length=400, blank=True)

    def __unicode__(self):
        return '%s, %s' % (self.workshop, self.person)
        
    class Meta:
        ordering = ['workshop', 'role', 'person']
