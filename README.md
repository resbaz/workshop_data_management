## Workshop Data Management

The Django application that makes up this project is found in wdm.

### Repository structure

The `production` branch the one that is "live", while we do our development
on the `master` branch.

### Importing data

There is a script for importing workshop participants in wdm/utils. It 
takes an Eventbrite csv dump of a workshop and a workshop id number as
arguments.

### UniMelb institutions

The following are useful notes about the institutions at the 
University of Melbourne:  
* In 2015, the departments of Zoology, Botany and Genetics merged to 
become the School of BioSciences
* The Walter and Eliza Hall Institute of Medical Research (WEHI) offer 
undergraduate, Honours and PhD places as the Department of Medical 
Biology in the Faculty of Medicine, Dentistry and Health Sciences

### Tutorial (status: on hold/deprecated for the moment)

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
