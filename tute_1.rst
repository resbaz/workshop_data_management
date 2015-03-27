=================================================
Learning practical databases via a Django web app
=================================================

Tutorial 1
==========

Preamble
--------

In the easy tutorial we really focused on getting up to speed with Django,
learning some easy concepts and language, and saw how easy it was to develop
a database with a web based front end.

One thing that we conveniently skirted around was data modelling and planning. 
I say convenient because these are two things that seem easy but are quite
hard and don't have definitive solutions.

In this tutorial we are going to look at those two things up front, because 
they help inform what we will be learning and make it easier to understand 
why we would use some of the special functions available within Django. 

It will also become clearer that the type of data we are looking at in this 
tutorial is much better suited to a database than a (multipage) spreadsheet.

------------------
What we will learn
------------------

Our use case will be how to keep track of students that attend workshops. We
want to collect data for smooth running on the day (eg, Dietary requirements),
but also for later analysis (Career Stage, Organisation affiliation, Age, 
Gender Identity). 

First we are going to do some mental work thinking about how to structure data.
In that process we will see how there are many ways to solve this problem, and 
that none of them are more correct than the other. However, there are some ways
that are more suited to the concepts and tools that are available to us in 
Django.

After thinking about how we will structure our data will start using those more
advanced tools and concepts to build a functioning web app that is suitably 
complex.

Traditionally, when we were thinking about the data we are going to collect, 
our framework has been the columns and rows of a spreadsheet, sometimes the 
extra pages. Usually a header row.

While this is still a good framework we are going to develop on top of that
with some broader ideas.

 #. What are we actually collecting?
 #. What are we trying to measure?
 #. How can I minimise my data entry? (which is a lazy, or human, way of 
    referring to the computer science theory of database normalization and 
    "Normal Forms")

As we walk through this example you will see how these three ideas inform what
structure we give our data. This tutorial can seem a little rambling and non 
linear - when thinking about data modelling it is worth investigating dead ends 
and backing out again to change tack.
 
I reiterate: there is rarely a "correct" answer to how your data should be
modelled, but there are ways that will make it easier to use, easier to enter 
and easier to think about. Sometimes that can lead to surprising results. 


Workshop Project
----------------

This project comes from a specific need we have within the Research Platforms 
and Research Bazaar organisational system. At first we started using a 
spreadsheet - a google doc - and it was fine. Suddenly it was three years later
and we had lots of information, but no easy way to navigate, analyse or 
summarise it.

So we decided to make a database with Django, given what we learned in the
beginners tutorial.

--------------
Data Modelling
--------------

Because we are modelling, we are just going to rough up a quick doc - we won't
actually build proper classes - this is still the thinking stage.

First, we will obviously need people. So let's create a Person class with the 
basic information that we want on them.

::
    
    class Person
        Name - CharField
        Other - CharField # for name in parent's language
        Email - EmailField


And we will want a Workshop for them to attend

::

    class Workshop
        Subject - CharField
        Date - DateField


How will these two object interact? Interesting question. 

First, there are three types of people that go to a workshop: students, 
instructors and helpers. Each of those groups need to be represented 
differently in the DB, because we will be gathering different information
on each of them.

There are a number of ways to approach this. 

 #. We can subclass Person three ways and relate them to the workshop
 #. We can just related the Person to the workshop three ways
 #. ?

I've already use the word **relate** twice, and SQL is a "relational database 
language" so lets take a quick look at what that means and how it works in 
Django.

In SQL databases, there are three types of relationships:

 * Many to Many: Any one Pizza can have many Toppings. Any one Topping can be on
   many Pizzas.
 * One to Many: Any one Manufacturer has many Cars, any one Car has one
   Manufacturer.
 * One to One: every one Person has one Genome Code, every one Genome Code 
   represents one Person. This is a very rare case that we use infrequently.

In Django these are represented as follows:
 
 * ManyToManyField 
 * ForeignKey (OneToMany, FK usually goes on the "one" side)
 * OneToOneField (essentially an FK with "unique=true" set)

Relational fields in Django are bi-directional, which means you can put them 
in either model. It will usually be apparent which model to put them in. Do we 
want a Workshop with Students or Students with a list of Workshops? And what 
type of relationship should we choose?

We know that a Workshop will have (hopefully) more than one Student, 
and that (hopefully) any Student will go to more than one Workshop, so
we will use a ManyToManyField as the relationship, and we will put it on the 
Workshop model.

Why? *My* thinking went like this:

1. Subclass Person, attach workshops. 

::

    class Student(Person)
        workshops - ManyToManyField(Workshop)

    class Helper(Person)
        workshops - ManyToManyField(Workshop)

    class Instructor(Person)
        workshops - ManyToManyField(Workshop)

or::

    class Student(Person)
        grade - CharField

    class Helper(Person)

    class Instructor(Person)
    
    class Workshop
        Subject - CharField
        Date - DateField
        students - ManyToManyField(Student)
        helpers - ManyToMany(Helper)
        instructors - ManyToMany(Instructor) #just in case


I didn't even finish typing before I thought - what about Ada Lovelace - she 
is a Student in one Workshop and an Instructor in another. Do I really want 
to have her in the DB twice, once each as a Student object and an Instructor
object? I could - there are no correct answers - but it does seem counter 
intiutive and feels like it would be harder to find full info about any 
particular person. 

2. Let's put the raw Person on the workshop instead

::

    class Workshop
        Subject - CharField
        Date - DateField
        students - ManyToManyField(Person)
        helpers - ManyToMany(Person)
        instructor - ManyToMany(Person) #just in case

Now we start thinking about how the that will work.

We will need to confirm that any particular person that is one type is not also
listed as another type - student Ada Lovelace cannot be in a workshop as a 
student *and* an instructor in the same workshop. So our options are now to
put in some validation code (ergh, boring) or re think our models.

While we are rethinking our models and looking over the data we have already 
collected, we realise we need an Organisational affiliation link per Person 
and we want to record each student's Career Stage so we can report what type of 
researchers are coming to our workshops.

This is easier to think about than the Workshop problem because it is distinct
and atomic. So we can just add it in quickly to clear it out of the way.

Let's give each Person an Organisation affliation, that's relatively easy. 

::

    class Organisation
        title - CharField
        location - CharField
        Department - CharField

    class Person
        Name - CharField
        Other - CharField
        Email - EmailField
        Org - ...

Ok. Damn. Thinking about the relationship between a Person and an Organisation
reminds us that it needs to be ManyToMany - any one Org has many People, 
and any one Person has (potentially) many Orgs - people move campuses, people
change departments, people change universities and employers. So now we have a 
new problem - which org is a Person at right now? Do we need to add a date 
field...ok this is getting messy.

<deep breath><jasmine tea><deep breath>

Let's go back to the very top of this tutorial and look at our guiding 
principles:

 #. What are we actually collecting?
 #. What are we trying to measure?
 #. How can I minimise my data entry? (which is a lazy, or human, way of 
    referring to the computer science theory of database normalization and 
    "Normal Forms")

The reason we want to know the Organisation of each Person is so that we can
report on **what type of students** are coming to our Workshops. 

Now that we think about it, Organisation is a data point that is related to 
the Person-Workshop relationship, not the Person individually. In fact, we
are also interested in the Career Stage of each Person, and this falls into 
exactly the same basket. That will change over time **but we only want it in
regards to our Workshop, not to the Person in particular**.

That makes things more interesting. Maybe this can solve both our problems -
how to relate the Person, the Workshop and how to record some extra data 
points.

Django has a special case called an **intermediate model** that is designed
to address this very thing. Let's look at how it works:

::

    class Instructor
        Workshop - ForeignKey(Workshop)
        Person - ForeignKey(Person)
        Organisation - FK(Organisation)
        Career Stage - ChoiceField

    class Helpers
        Workshop - FK(Workshop)
        Person - FK(Person)
        Organisation - FK(Organisation)
        Career Stage - ChoiceField

    class Students
        Workshop - FK(Workshop)
        Person - FK(Person)
        Grade - CharField
        Organisation - FK(Organisation)
        Career Stage - ChoiceField

    
It feels right just typing it out. We may find later that it is incorrect but 
for the moment it looks good. We can put a small validator on the Workshop 
model to check that a Person only performs one role per Workshop. 

Now that we are thinking about our data a little differently - we are 
collecting the Org data in a non obvious place, for instance, and we now have
the idea of a ManyToMany relationship having extra data, we start to see more
options.

For instance, of course we would like to measure attendance. To measure 
attendance we need a list of Applicants, so let's make a small change:

::

    class Students
        Workshop - FK(Workshop)
        Person - FK(Person)
        Grade - CharField
        Organisation - FK(Organisation)
        Career Stage - ChoiceField
        Attendance - BooleanField

    class Applicants
        Workshop - FK(Workshop)
        Person - FK(Person)
        ApplicationDate - DateField
        Organisation - FK(Organisation)
        Career Stage - ChoiceField

Why do we keep the Organisation and Career Stage information in the Student 
model. That's definitely a redundancy.

But what about the Student that is a drop in replacement? Or has a situational
change during the period between Application and the Workshop? It's worth 
keeping for those reasons. And, since we will be converting Applicants into 
Students automatically (seems like the best way to do it) we can just copy the 
data across, we won't have that much redundant labour (golden rule: redundant 
labour costs more than redundant disk space, which costs more than clean 
efficient models).

That's a solid base. Going back to our spreadsheet, we look at what else we 
need to collect and measure.

 * We want to measure gender distributions. 
 * We want to measure age distributions
 * Workshops sometimes have food. We need to know about dietary requirements
 * We want Workshops to have a little more info
 * We want to reduce typing, but also **increase** data accuracy (aka "reduce
   inaccurate data entry")

We can do that in one hit - here I'll present the final "thought experiment"
data models. As noted before, these may change as we go on, but we have to 
start somewhere.

In order to address the final point above, we will start to use Django's 
**choice field**. These will appear as a drop down list rather than a 
blank field.
 
The other points will be commented in the psuedo code

::

    GENDER_CHOICES = ( 
    ('m', 'Male'), 
    ('f', 'Female'), 
    ('o', 'Other'), 
    ) 

    class Person
        Name - CharField
        Other - CharField
        Email - EmailField
        DOB - DateField # age can be computed by (Workshop date - DOB)
        Gender Identity - CharField (choice=GENDER_CHOICES, default='o')
        # note that we think that an empty field here, so people can enter
        # what they personally identify as is best practice, but we are 
        # deliberately not allowing that to prevent spelling mistakes and
        # we really just want some person basics
    
    class Organisation
        title - CharField (choice = ORG_CHOICES) # long list, put at bottom.
        location - CharField (choices = dependant choices)
        Department - CharField (choices = dependat choices, DEPT_CHOICES for UoM)

    class Workshop
        Subject (title) - CharField
        Description (body text) - CharField # title might not be enough
        Date Held - DateField
        Teaching Hours - IntegerField
        Catering - BooleanField # do we provide lunch or a tea/coffe break

    class Instructor
        Workshop - FK(Workshop
        Person - FK(Person)
        Organisation - FK(Organisation)
        Career Stage - ChoiceField
        Dietary Requirements - ChoiceField 
        # we have moved Diet to the workshop as people's dietary req's may
        # change over time. We only need for this workshop.

    class Helpers
        Workshop - FK(Workshop)
        Person - FK(Person)
        Organisation - FK(Organisation)
        Career Stage - ChoiceField
        Dietary Requirements - ChoiceField

    class Students
        Workshop - FK(Workshop)
        Person - FK(Person)
        Grade - CharField
        Organisation - FK(Organisation)
        Career Stage - ChoiceField
        Attendance - BooleanField
        Dietary Requirements - ChoiceField

    class Applicants
        Workshop - FK(Workshop)
        Person - FK(Person)
        ApplicationDate - DateField
        Organisation - FK(Organisation)
        Career Stage - ChoiceField
        Dietary Requirements - ChoiceField

    # Other choices 

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
