=================================================
Learning practical databases via a Django web app
=================================================

Tutorial 2
==========

Preamble
--------

In the last tutorial we did a lot of thinking about how our data would look
from a database perspective. This is a valuable tool that will take some time
to perfect, but is a good start - seeing dead ends really helps.

In this tutorial we will be expanding our Django skills to the **presentation**
layer - ie, how our data will look in a web browser.

Once we have a general understanding of what tools are available to us, and how
our pages will look, we will be able to see what and where we are able to 
manipulate the **control** layer - how to manipulate the data to give us more
control at the presentation layer.

------------------
What we will learn
------------------

The first tutorial was largely based around app/models.py.

In this tutorial we will see with a few quick lines of code in urls.py and 
views.py, and an html template or two, how powerful Django really can be in 
bringing your data to the web for ease of use.


Workshop Project - Views
------------------------

When we think about how we will need to see our data, it should be apparent 
that there are really only a couple of ways that are strictly necessary:

 - the List View, where we can see all of our objects in a list. At some point
    it would be nice to filter that list as well.
 - the Detail View, where we can see the individual fields of any particular
    data object (Workshop, Participant, etc)
 - the Add/Update view, where an object can be added or an existing object 
    edited
 - not strictly necessary, but a nice caution, is a Delete View. We could just
    delete objects as required, but we have *all* experienced the joy of seeing
    the "are you sure" window. Let's build one of those too.


Given that this is all about the Workshop, let's start with Workshops as our
example model. 

The Django developers understand that the above five views are often required,
so they have made some generic version of each, to make our lives easier. Let's
take a look - open up views.py.

::

    from django.shortcuts import render

    # Create your views here.

Boring. Let's ignore the first line, and remove the second and get started.

::

    from django.shortcuts import render 
    from django.views.generic import DetailView, ListView 
    from django.views.generic.edit import CreateView, UpdateView, DeleteView 
     
    from .models import Workshop 
     
    ''' 
    Workshop Views 
    ''' 

Traditionally we put django imports together, and other imports below. The two
new lines of Django imports bring in those default generic views. The next 
brings in the Workshop model, and the last three lines are a comment - this 
file may get long because of the number of models, so it's good to mark our 
spot.


::

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

As you can see, that was not only easy, it is also self explanitory 

