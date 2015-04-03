""" models.py
    contains the models for:
    
"""

from django.db import models


GENDER_CHOICES = (
    ('m', 'Male'),
    ('f', 'Female'),
    ('o', 'Other'),
    )

ROLE_CHOICES = (
    ('i', 'Instructor'),
    ('h', 'Helper'),
    ('s', 'Student'),
    )

CAREER_CHOICES = (
    (1, 'Undergraduate'),
    (2, 'Honours'),
    (3, 'Masters'),
    (4, 'PhD - first year'),
    (5, 'PhD - second year'),
    (6, 'PhD - third year and beyond'),
    (7, 'Postdoc'),
    (8, 'Early career researcher'),
    (9, 'Mid career researcher'),
    (10, 'Senior researcher'),
    (11, 'Research assistant'),
    )

DIETARY_CHOICES = (
    (1, 'Vegetarian'),
    (2, 'Vegan'),
    (3, 'Gluten free'),
    (5, 'Lactose intolerant'),
    (6, 'Halal'),
    (7, 'Kosher'),
    )

CAMPUS_CHOICES = (
    (1, 'Parkville'),
    (2, 'Burnley'),
    (3, 'Albury-Wodonga'),
    (4, 'Wagga Wagga'),
    (5, 'Clayton'),    
    (6, 'Hobart'),
    (7, 'Burwood'),
    (8, 'Warrnambool'),
    (9, 'Ballarat'),
    (10, 'Gold Coast'),
    (11, 'Bendigo'),
    (12, 'Bundoora'),
    (13, 'Coffs Harbour'),
    (14, 'Hawthorn'),
    (15, 'Canberra'),
    (16, 'Sydney'),
    (17, 'Footscray'),
    (18, 'Cradle Coast'),
    )

# Parkville -> UniMelb, Monash
# Burnley -> UniMelb
# Albury-Wodonga -> Charles Sturt
# Wagga Wagga -> Charles Sturt
# Clayton -> CSIRO, Monash    
# Hobart -> CSIRO, UTAS
# Burwood -> Deakin
# Warrnambool -> Deakin
# Ballarat -> Federation Uni
# Gold Coast -> Griffith
# Bendigo -> La Trobe
# Bundoora -> La Trobe
# Coffs Harbour -> Southern Cross
# Hawthorn -> Swinburne
# Canberra -> UNSW
# Sydney -> UNSW
# Footscray -> Victoria Uni
# Cradle Coast -> UTAS


ORG_CHOICES = (
    (1,'Australian Antarctic Division'),
    (2,'Australian Astronomical Observatory'),
    (3,'Australian Catholic University'),
    (4,'Australian Institute of Marine Science'),
    (5,'Australian National Data Service'),
    (6,'Australian National University'),
    (7,'Australian Nuclear Science and Technology Organisation'),
    (8,'Baker IDI Heart and Diabetes Institute'),
    (9,'Bionics Institute'),
    (10,'Bureau of Meteorology'),
    (11,'Burnet Institute'),
    (12,'Charles Sturt University'),
    (13,'CSIRO'),
    (14,'Curtin University of Technology'),
    (15,'Deakin University'),
    (16,'Edith Cowan University'),
    (17,'Federation University'),
    (18,'Fred Hollows Foundation'),
    (19,'Griffith University'),
    (20,'IBM Research'),
    (21,'James Cook University'),
    (22,'La Trobe University'),
    (23,'Macquarie University'),
    (24,'Monash Alfred Psychiatry Research Centre'),
    (25,'Monash University'),
    (26,'Murdoch Childrens Research Institute'),
    (27,'Museum Victoria'),
    (28,'New Zealand eScience Infrastructure'),
    (29,'Peter MacCallum Cancer Centre'),
    (30,'Queensland Government'),
    (31,'Queensland University of Technology'),
    (32,'RMIT'),
    (33,'Software Sustainability Institute'),
    (34,'Southern Cross University'),
    (35,'Swinburne University of Technology'),
    (36,'University of Adelaide'),
    (37,'University of Auckland'),
    (38,'University of Canterbury'),
    (39,'University of Melbourne'),
    (40,'University of New England'),
    (41,'University of Otago'),
    (42,'University of Queensland'),
    (43,'University of Southern Queensland'),
    (44,'University of Sydney'),
    (45,'University of Tasmania'),
    (45,'University of Technology Sydney'),
    (46,'University of the Sunshine Coast'),
    (47,'University of Western Australia'),
    (48,'University of Western Sydney'),
    (49,'University of Wollongong'),
    (50,'UNSW'),
    (51,'Victoria University'),
    (52,'Walter and Eliza Hall Institute of Medical Research'),
    )

DEPT_CHOICES = (
    (1,'Faculty of Architecture, Building and Planning'),
    (2,'Melbourne School of Design'),
    (3,'Faculty of Arts'),
    (4,'Asia Institute'),
    (5,'School of Culture and Communication'),
    (6,'School of Historical and Philosophical Studies'),
    (7,'School of Languages and Linguistics '),
    (8,'School of Social and Political Sciences'),
    (9,'Graduate School of Humanities and Social Sciences'),
    (10,'Faculty of Business and Economics'),
    (11,'Melbourne Business School'),
    (12,'Melbourne School of Government'),
    (13,'The Melbourne Institute'),
    (14,'Department of Accounting'),
    (15,'Department of Business Administration'),
    (16,'Department of Economics'),
    (17,'Department of Finance'),
    (18,'Department of Management and Marketing'),
    (19,'Melbourne Graduate School of Education'),
    (20,'Melbourne School of Engineering'),
    (21,'Department of Biomedical Engineering'),
    (22,'Department of Chemical and Biomolecular Engineering'),
    (23,'Department of Computing and Information Systems'),
    (24,'Department of Electrical and Electronic Engineering'),
    (25,'Department of Infrastructure Engineering'),
    (26,'Department of Mechanical Engineering'),
    (27,'Melbourne School of Information'),
    (28,'Melbourne Law School'),
    (29,'Faculty of Medicine, Dentistry and Health Sciences'),
    (30,'Melbourne Dental School'),
    (31,'Melbourne Medical School'),
    (32,'Department of Anatomy and Neuroscience'),
    (33,'Department of Biochemistry and Molecular Biology'),
    (34,'General Practice and Primary Health Care Academic Centre'),
    (35,'Health and Biomedical Informatics Unit'),
    (36,'Medical Education Unit'),
    (37,'Department of Medicine at Austin Health'),
    (38,'Department of Medicine at Royal Melbourne Hospital'),
    (39,'Department of Medicine at St Vincents'),
    (40,'Department of Microbiology and Immunology'),
    (41,'NorthWest Academic Centre'),
    (42,'Department of Obstetrics and Gynaecology'),
    (43,'Department of Ophthalmology'),
    (44,'Department of Otolaryngology'),
    (45,'Department of Pathology'),
    (46,'Department of Paediatrics'),
    (47,'Pharmacology and Therapeutics'),
    (48,'Department of Physiology'),
    (49,'Department of Psychiatry'),
    (50,'Department of Radiology'),
    (51,'Rural Health Academic Centre'),
    (52,'Department of Surgery at Austin Health'),
    (53,'Department of Surgery at Royal Melbourne Hospital'),
    (54,'Department of Surgery at St Vincents'),
    (55,'Melbourne School of Health Sciences'),
    (56,'Department of Nursing'),
    (57,'Department of Physiotherapy'),
    (58,'Department of Social Work'),
    (59,'Department of Audiology and Speech Pathology'),
    (60,'Melbourne School of Population and Global Health'),
    (61,'Melbourne School of Psychological Sciences'),
    (62,'Florey Institute of Neuroscience and Mental Health'),
    (63,'Faculty of Science'),
    (64,'School of Botany'),
    (65,'School of Chemistry'),
    (66,'School of Earth Sciences'),
    (67,'Department of Genetics'),
    (68,'Department of Mathematics and Statistics'),
    (69,'Department of Optometry and Vision Sciences'),
    (70,'School of Physics'),
    (71,'Department of Zoology'),
    (72,'bio21'),
    (73,'Faculty of Veterinary and Agricultural Sciences'),
    (74,'Faculty of Victorian College of the Arts and Melbourne Conservatorium of Music'),
    (75,'Melbourne School of Land and Environment'),
    (76,'Department of Agriculture and Food Systems'),
    (77,'Department of Forest and Ecosystem Science'),
    (78,'Department of Resource Management and Geography'),
    (79,'Scholarly Information'),
    (80,'VLSCI'),
    )


class Person(models.Model):
    """The underlying model for a person."""

    name = models.CharField(max_length=128)
    email = models.EmailField()
    gender = models.CharField(u'gender', max_length=2, choices=GENDER_CHOICES, default='o')
    dob = models.DateField(u'Date of Birth', blank=True, null=True)    


class Workshop(models.Model):
    """The underlying model for workshops."""

    title = models.CharField(u'title', max_length=100)
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    teaching_hours = models.IntegerField()
    catering = models.BooleanField(default=False)

    class Meta:
        ordering = ['start_date',]


class Participant(models.Model):
    """Intermediate class for workshop participants."""

    workshop = models.ForeignKey(Workshop)
    person = models.ForeignKey(Person)
    role = models.CharField(u'role', max_length=2, choices=ROLE_CHOICES)
 
    institution = models.CharField(u'institution', max_length=3, choices=ORG_CHOICES)
    campus = models.CharField(u'campus', max_length=3, choices=CAMPUS_CHOICES)
    department = models.CharField(u'department', max_length=3, choices=DEPT_CHOICES, blank=True)
    
    career_stage = models.CharField(u'career stage', max_length=4, choices=CAREER_CHOICES)
    dietary_requirements = models.CharField(u'dietary requirements', max_length=2, choices=DIETARY_CHOICES)
    
    offer = models.BooleanField(default=False)        # Were the offered a ticket?
    acceptance = models.BooleanField(default=False)   # Did they accept the offer?
    attendance = models.BooleanField(default=False)   # Did they actually attend?




