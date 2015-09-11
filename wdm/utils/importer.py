#!/usr/bin/env python

"""
Import participant data for a single workshop.
"""

import os, sys, pdb
import csv
import argparse

from django.core.exceptions import ObjectDoesNotExist
from workshops.models import Institution, Participant, Person, Workshop

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
    old_notes = person.notes
    logfile.write("Notes updated: %s has had %s added to their notes \n", %(person, entry))
    person.notes = old_notes + ', ' + entry 
    person.save()

def main(infile_name, workshop_index):

    # Make sure the workshop index is correct
    try:
        ws = Workshop.objects.get(id=workshop_index)
    except:
        print "There's been an error finding the Workshop"
        sys.exit(1)

    # Create a log file to keep track of unidentified participants
    logfile = open('import.log', 'w')


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
            
            if created:
                old_mobile = new_person.mobile
                old_dob = new_person.dob
                old_gender = new_person.gender

            mobile = row[13]
            if len(mobile) > 0:
                if mobile[0] == '0':
                    pass
                elif mobile[0] == '+':
                    pass
                elif mobile[0] == '8' or mobile[0] == '9':
                    mobile = ''.join(('03',mobile))
                else:
                    mobile = ''.join(('0',mobile))
                if created or len(old_mobile) < 1:
                    new_person.mobile = mobile
                elif mobile != old_mobile:
                    update_notes(new_person, old_mobile)
                    new_person.mobile = mobile
                else:
                    logfile.write("dammit, mobile phone corner case problems for %s \n", %name)

            dob = row[14]
            '''age = row[14]
            if len(age) > 0:
                dob = datetime.date(datetime.datetime.now().year-age, 1, 1)      
            '''
            if len(dob)>0:
                if created:
                    new_person.dob = dob
                elif old_dob != dob:
                    update_notes(new_person, old_dob)    
                    new_person.dob = dob
                else:
                    logfile.write("dammit, dob corner case problems for %s \n", %name)

            gender = row[15]
            if len(gender) > 0:
                g = gender[0].lower()
                if created or old_gender == g:
                    new_person.gender = g
                elif:
                    update_notes(new_person, old_gender) 
                    new_person.gender = g
                else:
                    logfile.write("dammit, gender corner case problems for %s \n", %name)
            
            new_person.save()
            
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

            for x in CAREER_CHOICES:
                if x[1] == row[25]
                career = x[0]
                
            new_participant = Participant(person=new_person, institution=temp_institution, role='s', career_stage=career, workshop=ws)

            attend_status = row[12]
            if attend_status == 'Checked In':
                new_participant.attendance_start = True
                new_participant.attendance_end = True
            if attend_status == 'Attending':
                new_participant.attendance_start = False 
                new_participant.attendance_end = False
            
            new_participant.save()

if __name__ == '__main__':
    
    description = 'Import participant data from a csv file for a single workshop.'
    parser = argparse.ArgumentParser(description=description,
                                     epilog=extra_info, 
                                     argument_default=argparse.SUPPRESS,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("infile", type=str, help="Input file name")
    parser.add_argument("workshop_index", type=int, help="Database index of the workshop")

    args = parser.parse_args()

    main(args.infile, args.workshop_index)
