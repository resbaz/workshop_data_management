-------------------------------
Models needed with descriptions
-------------------------------

Top level Objects
=================

Class Person
------------

''' ID Fields '''
Name  - CharField
Other - CharField
Email - EmailField

''' Metadata '''

.. note::
    ChoiceFields are described at the bottom of this document

Gender Identity - ChoiceField
DOB - DateField
Dietary Requirements - ChoiceField


Class Organisation
------------------

Title - CharField (choices = ORG_CHOICES)
Location - ChoiceField (choices = dependant choices)
Department - ChoiceField(choices = dependat choices, DEPT_CHOICES for UoM)


Class Workshop
--------------

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
''' Intermediate class '''
Workshop - FK(Workshop)
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
''' Intermediate class that links helpers with the workshops they helped with '''
Workshop - FK(Workshop)
Person - FK(Person)
Organisation - FK(Organisation)
Career Stage - ChoiceField

Class Students
--------------
''' Intermediate class '''
Workshop - FK(Workshop)
Person - FK(Person)
Grade - CharField
Attendance - BooleanField
Organisation - FK(Organisation)
Career Stage - ChoiceField

Class Applicants
----------------
''' Intermediate class '''
Workshop - FK(Workshop)
Person - FK(Person)
ApplicationDate - DateField
Organisation - FK(Organisation)
Career Stage - ChoiceField

Choice Fields for restricted data entry
=======================================

CAREER_CHOICES = (

)



GENDER_CHOICES = (
'm', 'Male',
'f', 'Female',
'o', 'Other',
)

ORG_CHOICES = (
Australian Antarctic Division
Australian Astronomical Observatory
Australian Catholic University
Australian Institute of Marine Science
Australian National Data Service
Australian National University
Australian Nuclear Science and Technology Organisation
Baker IDI Heart and Diabetes Institute
Bionics Institute
Bureau of Meteorology
Burnet Institute
Charles Sturt University (Albury-Wodonga)
Charles Sturt University (Wagga Wagga)
CSIRO (Clayton)
CSIRO (Hobart)
Curtin University of Technology
Deakin University (Burwood)
Deakin University (Warrnambool)
Edith Cowan University
Federation University (Ballarat)
Fred Hollows Foundation
Griffith University
Griffith University (Gold Coast)
IBM Research
James Cook University
La Trobe University (Bendigo)
La Trobe University (Bundoora)
Macquarie University
Monash Alfred Psychiatry Research Centre
Monash University (Clayton)
Monash University (Parkville)
Murdoch Childrens Research Institute
Museum Victoria
New Zealand eScience Infrastructure
Peter MacCallum Cancer Centre
Queensland Government (Department of Agriculture, Fisheries an Forestry)
Queensland University of Technology
RMIT
Software Sustainability Institute
Southern Cross University (Coffs Harbour)
Swinburne University of Technology (Hawthorn)
University of Adelaide
University of Auckland
University of Canterbury
University of Melbourne (Burnley)
University of Melbourne (Parkville)
University of New England
University of Otago
University of Queensland
University of Southern Queensland
University of Sydney
University of Tasmania (Cradle Coast)
University of Tasmania (Hobart)
University of Technology, Sydney
University of the Sunshine Coast
University of Western Australia
University of Western Sydney
University of Wollongong
UNSW (Canberra)
UNSW (Sydney)
Victoria University (Footscray)
Walter and Eliza Hall Institute of Medical Research
)

DEPT_CHOICES = (
Faculty of Architecture, Building and Planning
Melbourne School of Design
Faculty of Arts
Asia Institute
School of Culture and Communication
School of Historical and Philosophical Studies
School of Languages and Linguistics 
School of Social and Political Sciences
Graduate School of Humanities and Social Sciences
Faculty of Business and Economics
Melbourne Business School
Melbourne School of Government
The Melbourne Institute
Department of Accounting
Department of Business Administration
Department of Economics
Department of Finance
Department of Management and Marketing
Melbourne Graduate School of Education
Melbourne School of Engineering
Department of Biomedical Engineering
Department of Chemical and Biomolecular Engineering
Department of Computing and Information Systems
Department of Electrical and Electronic Engineering
Department of Infrastructure Engineering
Department of Mechanical Engineering
Melbourne School of Information
Melbourne Law School
Faculty of Medicine, Dentistry and Health Sciences
Melbourne Dental School
Melbourne Medical School
Department of Anatomy and Neuroscience
Department of Biochemistry and Molecular Biology
General Practice and Primary Health Care Academic Centre
Health and Biomedical Informatics Unit
Medical Education Unit
Department of Medicine at Austin Health
Department of Medicine at Royal Melbourne Hospital
Department of Medicine at St Vincent's
Department of Microbiology and Immunology
NorthWest Academic Centre
Department of Obstetrics and Gynaecology
Department of Ophthalmology
Department of Otolaryngology
Department of Pathology
Department of Paediatrics
Pharmacology and Therapeutics
Department of Physiology
Department of Psychiatry
Department of Radiology
Rural Health Academic Centre
Department of Surgery at Austin Health
Department of Surgery at Royal Melbourne Hospital
Department of Surgery at St Vincent’s
Melbourne School of Health Sciences
Department of Nursing
Department of Physiotherapy
Department of Social Work
Department of Audiology and Speech Pathology
Melbourne School of Population and Global Health
Melbourne School of Psychological Sciences
Florey Institute of Neuroscience and Mental Health
Faculty of Science
School of Botany
School of Chemistry
School of Earth Sciences
Department of Genetics
Department of Mathematics and Statistics
Department of Optometry and Vision Sciences
School of Physics
Department of Zoology
bio21
Faculty of Veterinary and Agricultural Sciences
Faculty of Victorian College of the Arts and Melbourne Conservatorium of Music
Melbourne School of Land and Environment
Department of Agriculture and Food Systems
Department of Forest and Ecosystem Science
Department of Resource Management and Geography
Scholarly Information
VLSCI
)

