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

Our use case will be how to keep track of students that attend workshops. First
we are going to do some mental work thinking about how to structure data. In 
that process we will see how there are many ways to solve this problem, and that
none of them are more correct than the other. However, there are some ways that
are more suited to the concepts and tools that are available to us in Django.

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
structure we give our data. This tutorial can seem a little rambling - when 
thinking about data modelling it is worth investigating dead ends and backing 
out again to change tack. 

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
        Other - CharField
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


I've already use the word relate twice, and SQL is a "relational database 
language" so lets take a quick look at what that means and how it works in 
Django.

In SQL databases, there are three types of relationships:

 * One to One: every one Person has one Genome code, every one Genome code 
   represents one person. This is a very rare case that we use infrequently.
 * One to Many: Any one Manufacturer has many cars, any one car has one
   Manufacturer.
 * Many to Many: Any one Piza can have many toppings. Any one topping can be on
   many Pizzas.


Relational fields in Django are bi-directional, so you can put them in 
either model. It will usually be apparent which model to put them in. Do we 
want a Workshop with students or students with a list of workshops? And what 
kind of relationship?


We know that a Workship will have (hopefully) more than one student, 
and that (hopefully) any student will go to more than one Workshop, so
we will use a ManyToManyField as the relationship, and we will put it on the 
Workshop model.

::

    class Workshop
        Subject - CharField
        Date - DateField
        students - ManyToManyField(Person)

Each Workshop will also have an (or...?) Instructor, and some helpers:

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

Are there any other reasons for rethinking our models? Well, Ada might well
be a student in one workshop and an instructor in another - so maybe we now
want to move the Workshop into the Person model (the relationship direction
we talked about above). 

While we are looking over the data we have collected, we realise we need an
Organisational affiliation link per person and we want to record each students
Career stage so we can report what type of researchers are coming to our 
workshops.

So let's give each Person an Organisation affliation, that's relatively easy. 






Most people will be students, but some students may go on to become helpers 
or instructors. Hmm.






























