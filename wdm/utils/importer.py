#!/usr/bin/env python

"""
Import participant data for a single workshop.
"""

import os, sys, pdb
import django
import csv
import argparse
import datetime

sys.path.append('/home/ubuntu/www/dev/wdm/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workshop_data_management.settings.local")
django.setup()

from django.conf import settings

from django.core.exceptions import ObjectDoesNotExist
from workshops.models import Institution, Participant, Person, Workshop

from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from django.utils import timezone
from django.conf import settings
from django.core.cache import cache
from django.db.models import Avg, Count, F, Max, Min, Sum, Q, Prefetch
from django.core.urlresolvers import reverse
from django.db import transaction

cwd = os.getcwd()
sys.path.append(cwd)

rownum = 0
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
    ('13', 'Professional'),
    )

def update_notes(person, entry):
    """Update a Person's notes field."""
    import logging
    logger = logging.getLogger('importer')
    old_notes = person.notes
    logger.info("Notes updated: %s has had %s added to their notes \n" % (person, entry))
    person.notes = old_notes + ', ' + str(entry)
    person.save()

def main(infile_name, workshop_index):
    import logging
    logger = logging.getLogger('importer')
    
    # Make sure the workshop index is correct
    try:
        ws = Workshop.objects.get(id=workshop_index)
    except:
        print "There's been an error finding the Workshop"
        sys.exit(1)

    # Create a log file to keep track of unidentified participants
    logger.info("logs for workshop: %s" % ws )

    #with open('/home/ubuntu/rp_matlab_20150608.csv','rb') as csvfile:
    with open(infile_name,'rb') as csvfile:
        reader= csv.reader(csvfile)
        headers = reader.next()
        for row in reader:
            # combine first and last name into "name"
            # get_or_create person based on case insensitive(name) and email
            name = []
            name.append(row[3])
            name.append(row[4])
            name = ' '.join(name)
            
            email = row[5]
            
            # When looking for people objects, we can't assume that name=name is
            # sufficient - there can be many Jane Smiths. It's better to get 
            # duplication when people enter new email addresses, than collapse
            # distinct people into a single entity.
            new_person, created = Person.objects.get_or_create(name=name, email=email)
            
            if not created:
                old_mobile = new_person.mobile
                old_dob = new_person.dob
                old_gender = new_person.gender
            else:
                old_mobile=old_dob=old_gender=""


            mobile = row[13]
            if len(mobile) > 0:
                if mobile[0] == '0':
                    pass
                elif mobile[0] == '+' or mobile[0] == '6':
                    pass
                elif mobile[0] == '8' or mobile[0] == '9':
                    mobile = ''.join(('03',mobile))
                else:
                    mobile = ''.join(('0',mobile))
                if created:
                    new_person.mobile = mobile
                elif mobile != old_mobile:
                    update_notes(new_person, old_mobile)
                    new_person.mobile = mobile
                else:
                    logger.debug("dammit, mobile phone corner case problems for %s \n" % name)

            age = row[14]
            if len(age)>0:
                dob = datetime.date(datetime.datetime.now().year-int(age), 1, 1)      
                if created:
                    new_person.dob = dob
                elif old_dob != dob:
                    update_notes(new_person, old_dob)    
                    new_person.dob = dob
                else:
                    logger.debug("dammit, dob corner case problems for %s \n" % name)
            '''
            dob = row[14]
            if len(dob)>0:
                iso8601 = datetime.datetime.strptime(dob,'%d/%m/%y').strftime('%Y-%m-%d')
                if created:
                    new_person.dob = iso8601
                elif old_dob != iso8601:
                    update_notes(new_person, old_dob)    
                    new_person.dob = iso8601
                else:
                    logger.debug("dammit, dob corner case problems for %s \n" % name)
            '''
            gender = row[15]
            if len(gender) > 0:
                g = gender[0].lower()
                if created or old_gender == g:
                    new_person.gender = g
                elif old_gender != g:
                    update_notes(new_person, old_gender) 
                    new_person.gender = g
                else:
                    logger.debug("dammit, gender corner case problems for %s \n" % name)
            
            
            try:
                new_person.save()
                logger.info("saved Person %s" % new_person)
            except Exception as e:
                logger.warning("Exception: %s, %s" %(e.__doc__, e.message))
                 
            
            # Get the Institute, to make the participant
            # Institutions are hard and should probably be remodelled/refactored
            #at the moment, we are setting all to TEMP and researchers are to fix
            '''
            reported_organisation = row[16]
            reported_department = row[17]

            reported_institution = Institution.objects.get(organisation=reported_organisation, department=reported_department)
            
            if not reported_institution:
                reported_institution = Institution.objects.filter(organisation=reported_organisation)
            if not reported_institution or len(reported_institution) > 0:
                reported_institution = Institution.objects.get(organisation="TEMP_IMPORT")
            '''                
            
            temp_institution = Institution.objects.get(organisation="TEMP_IMPORT")
            career = ""
            for x in CAREER_CHOICES:
                if x[1] == row[20]:
                   career = x[0]
            if career == "":
                logger.debug("Career stage is unusual, please check original: %s: %s" %(name, row[20]))
 
            new_participant = Participant(person=new_person, institution=temp_institution, role='s', career_stage=career, workshop=ws)

            attend_status = row[12]
            if attend_status == 'Checked In':
                new_participant.attendance_start = True
                new_participant.attendance_end = True
            if attend_status == 'Attending':
                new_participant.attendance_start = False 
                new_participant.attendance_end = False
            
            try:
                new_participant.save()
                logger.info("saved Participant %s" % new_participant)
            except Exception as e:
                logger.warning("Exception: %s, %s" %(e.__doc__, e.message))

if __name__ == '__main__':
    
    description = 'Import participant data from a csv file for a single workshop.'
    parser = argparse.ArgumentParser(description=description,
                                     epilog="epilog", 
                                     argument_default=argparse.SUPPRESS,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("infile", type=str, help="Input file name")
    parser.add_argument("workshop_index", type=int, help="Database index of the workshop")

    args = parser.parse_args()

    main(args.infile, args.workshop_index)
