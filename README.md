## Workshop Data Management

This project is a combination of practical and educational - we are creating a
small web based database application for the management of the Research 
Platforms workshops, to provide some broad stroke analysis of those workshops,
and also to be a real world tutorial for an intro to data modelling and a more
difficult Django, one that is harder than most regular tutorials, and our 
[introduction tutorial](https://github.com/datakid/django-tutorial).

The file `modelling.rst` was created by Damien and I just bashing out ideas of 
what the data should look like. It's an initial take that may change as the
project develops.

The first tutorial is based on the that file and the ideas that Damien and I
had that lead to the models.

### Repository structure

The `production` branch the one that is "live", while we do our development
on the `master` branch.

### Importing data

Data in .csv format can be imported via the admin interface
(we've used the django [import-export](https://django-import-export.readthedocs.org/en/latest/) library).
Here's a few notes on that process:  
* True and False values must be represented by a 1 and 0 respectively
* There must be a header row in the csv file which matches the name of the model fields
(and the first column must be "id")
* For fields where you are selecting an existing entry in the database 
or choosing from pre-set choices, you must specify the id

### UniMelb institutions

The following are useful notes about the institutions at the University of Melbourne:  
* In 2015, the departments of Zoology, Botany and Genetics merged to become the School of BioSciences
* The Walter and Eliza Hall Institute of Medical Research (WEHI) offer undergraduate, Honours and PhD places as the Department of Medical Biology in the Faculty of Medicine, Dentistry and Health Sciences


