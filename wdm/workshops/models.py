""" models.py
    contains the models for:
    
"""

from django.core.urlresolvers import reverse
from django.db import models
from django.utils.text import slugify


GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Other'),
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
    )

DIETARY_CHOICES = (
    ('1', 'Vegetarian'),
    ('2', 'Vegan'),
    ('3', 'Gluten free'),
    ('5', 'Lactose intolerant'),
    ('6', 'Halal'),
    ('7', 'Kosher'),
    )


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

    slug = models.SlugField(max_length=128, null=True, blank=True)

    def __unicode__(self):
        return '%s' % (self.name)

    def get_absolute_url(self):
        return reverse('person_detail', args=[self.slug])
        
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Person, self).save()

    def first_letter(self):
        first, last = self.name.split(' ',1)
        return last[0].upper() or ''
    
    class Meta:
        ordering = ['name', ]
        

class Workshop(models.Model):
    """Underlying model for workshops."""

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400, blank=True)
    start_date = models.DateField()
    teaching_hours = models.FloatField()
    catering = models.BooleanField(default=False)
    
    website = models.URLField(blank=True)
    blog_post = models.URLField(blank=True)
   
    slug = models.SlugField(max_length=115, blank=True)   
 
    def __unicode__(self):
        return '%s: %s' % (self.start_date, self.title)
    
    def get_absolute_url(self):
        return reverse('workshop_detail', args=[self.slug])

    def total_attendance(self):
        return self.participant_set.all().count()
   
    def career_stats(self):
        career_stats = {}
        for stage_id, stage in CAREER_CHOICES:
            career_stats[stage_id]=self.participant_set.filter(career_stage=stage_id).count()
        return career_stats

    def save(self):
        """This creates the slug automagically from the date and title"""
        if not self.slug:
            temp = "%s %s" %(self.start_date, self.title)
            self.slug = slugify(temp)
        super(Workshop, self).save()    

    class Meta:
        ordering = ['start_date',]


class Institution(models.Model):
    """Underlying model for institutions."""
    
    organisation = models.CharField(max_length=100)
    campus = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=200, blank=True)

    def __unicode__(self):
        return '%s (%s), %s' % (self.organisation, 
                                self.campus,
                                self.department)

    def get_absolute_url(self):
        return reverse('institution_detail', args=[self.slug])

    def save(self):
        if not self.slug:
             self.slug = slugify(self)
        super(Institution, self).save()

    class Meta:
        ordering = ['organisation', 'department']
    

class Participant(models.Model):
    """Intermediate class for workshop participants."""

    person = models.ForeignKey(Person)
    workshop = models.ForeignKey(Workshop)
    institution = models.ForeignKey(Institution)

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
