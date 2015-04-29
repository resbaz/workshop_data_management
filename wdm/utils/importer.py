from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from workshops.models import Institution, Participant, Person, Workshop
from django.utils import timezone
from django.conf import settings
from django.core.cache import cache
from django.db.models import Avg, Count, F, Max, Min, Sum, Q, Prefetch
from django.core.urlresolvers import reverse
from django.db import transaction

import os
import csv

logfile = open('import.log', 'w')

personlist = {}
people = Person.objects.all()
for person in people:
    personlist[person.name] = {'id':person.id, 'Name': + person.name, 'email': person.email}

temp_inst = Institute.objects.get(id=98)
workshop_index = sys.argv[1]
try:
    ws = Workshop.objects.get(id=workshop_index)
except:
    print "There's been an error finding the Workshop"
    sys.exit(1)



with open('XXXX.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # this is where we do the main check, data entry and save of participant
        fname = row[0]
        sname = row[1]
        name = fname + " " + sname
        
        email = row[2]
        if name in personlist.keys():
            if personlist[name]['email'] not '':
               # add email to newp.email
            else:   
               # append email to newp.notes
        else: #person doesn't exist
            logfile.write(row)        


        # create new participant
        newp = Participant()
        newp.workshop = ws
        newp.institution = temp_inst
        newp.role = 't'
                

 
        
