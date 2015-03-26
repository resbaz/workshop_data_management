-------------------------------
Models needed with descriptions
-------------------------------
=================
Top level Objects
=================

Class Person
------------

ID Fields
=========
::

    Name  - CharField
    Other - CharField
    Email - EmailField

Metadata
========

.. ..

.. note::
    ChoiceFields are described at the bottom of this document

..

::
    
    Gender Identity - ChoiceField
    DOB - DateField
    Dietary Requirements - ChoiceField


Class Organisation
------------------
::

    Title - CharField (choices = ORG_CHOICES)
    Location - ChoiceField (choices = dependant choices)
    Department - ChoiceField(choices = dependat choices, DEPT_CHOICES for UoM)


Class Workshop
--------------

::

    Subject (title) - CharField
    Description (body text) - CharField

    Date Held - DateField
    Teaching Hours - IntegerField

    Catering - BooleanField

.. note::
    '''
    Instructors - Many-to-Many-Field
    Helpers - Many-to-ManyField
    Students - Many-to-ManyField
    Originally we had these fields on the Workshop. But then we started to think about some
    Instructors or Helpers in one subject could be students in another and vice versa. So we
    have taken these out and created an intermediatory class for each.
    See here for more on intermediatory classes
    https://docs.djangoproject.com/en/1.7/topics/db/models/#extra-fields-on-many-to-many-relationships
    '''

Class Instructors
-----------------
''' Intermediate class ''' ::

    Workshop - FK(Workshop
    Person - FK(Person)
    Organisation - FK(Organisation)
    Career Stage - ChoiceField

.. note::
    '''
    Originally we had the Org on the Person model, but realised that would
    skew our data because a person may belong to a number of orgs and we
    are looking to distinguish *per workshop*. Hence moving the org data
    to these intermediate classes. 
    '''

Class Helpers
-------------
''' Intermediate class that links helpers with the workshops they helped with ''' ::

    Workshop - FK(Workshop)
    Person - FK(Person)
    Organisation - FK(Organisation)
    Career Stage - ChoiceField

Class Students
--------------
''' Intermediate class ''' ::

    Workshop - FK(Workshop)
    Person - FK(Person)
    Grade - CharField
    Attendance - BooleanField
    Organisation - FK(Organisation)
    Career Stage - ChoiceField

Class Applicants
----------------
''' Intermediate class ''' ::

    Workshop - FK(Workshop)
    Person - FK(Person)
    ApplicationDate - DateField
    Organisation - FK(Organisation)
    Career Stage - ChoiceField

Choice Fields for restricted data entry
=======================================

::
    CAREER_CHOICES = (

    )

:: 

    GENDER_CHOICES = (
    'm', 'Male',
    'f', 'Female',
    'o', 'Other',
    )

::

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
    (12,'Charles Sturt University (Albury-Wodonga)'),
    (13,'Charles Sturt University (Wagga Wagga)'),
    (14,'CSIRO (Clayton)'),
    (15,'CSIRO (Hobart)'),
    (16,'Curtin University of Technology'),
    (17,'Deakin University (Burwood)'),
    (18,'Deakin University (Warrnambool)'),
    (19,'Edith Cowan University'),
    (20,'Federation University (Ballarat)'),
    (21,'Fred Hollows Foundation'),
    (22,'Griffith University'),
    (23,'Griffith University (Gold Coast)'),
    (24,'IBM Research'),
    (25,'James Cook University'),
    (26,'La Trobe University (Bendigo)'),
    (27,'La Trobe University (Bundoora)'),
    (28,'Macquarie University'),
    (29,'Monash Alfred Psychiatry Research Centre'),
    (30,'Monash University (Clayton)'),
    (31,'Monash University (Parkville)'),
    (32,'Murdoch Childrens Research Institute'),
    (33,'Museum Victoria'),
    (34,'New Zealand eScience Infrastructure'),
    (35,'Peter MacCallum Cancer Centre'),
    (36,'Queensland Government (Department of Agriculture, Fisheries an Forestry)'),
    (37,'Queensland University of Technology'),
    (38,'RMIT'),
    (39,'Software Sustainability Institute'),
    (40,'Southern Cross University (Coffs Harbour)'),
    (41,'Swinburne University of Technology (Hawthorn)'),
    (42,'University of Adelaide'),
    (43,'University of Auckland'),
    (44,'University of Canterbury'),
    (45,'University of Melbourne (Burnley)'),
    (46,'University of Melbourne (Parkville)'),
    (47,'University of New England'),
    (48,'University of Otago'),
    (49,'University of Queensland'),
    (50,'University of Southern Queensland'),
    (51,'University of Sydney'),
    (52,'University of Tasmania (Cradle Coast)'),
    (53,'University of Tasmania (Hobart)'),
    (54,'University of Technology, Sydney'),
    (55,'University of the Sunshine Coast'),
    (56,'University of Western Australia'),
    (57,'University of Western Sydney'),
    (58,'University of Wollongong'),
    (59,'UNSW (Canberra)'),
    (60,'UNSW (Sydney)'),
    (61,'Victoria University (Footscray)'),
    (62,'Walter and Eliza Hall Institute of Medical Research'),
    )

::

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
    (39,'Department of Medicine at St Vincent's'),
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
    (54,'Department of Surgery at St Vincent’s'),
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

