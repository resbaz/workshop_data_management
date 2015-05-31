#!/usr/bin/env python

"""
Import participant data for a single workshop.

"""

import os, sys, pdb
import csv
import argparse

cwd = os.getcwd()
sys.path.append(cwd)

from workshops.models import Institution, Participant, Person, Workshop


def update_notes(person, entry):
    """Update a Person's notes field."""

    old_notes = person.notes
    person.notes = old_notes + ' ' + entry 
    person.save()


def main(infile_name, workshop_index):
    """Run the program."""

    # Make sure the workshop index is correct
    try:
        ws = Workshop.objects.get(id=workshop_index)
    except:
        print "There's been an error finding the Workshop"
        sys.exit(1)

    # Create a log file to keep track of unidentified participants
    logfile_name = infile_name.split('.')[0]+'.log'
    logfile = open(logfile_name, 'w')

    # Create a temporary institute entry that will be updated manually later
    # 98 is TEMP_IMPORT, 90 is UMelb, Unknown
    temp_institute = Institution.objects.get(id=98)

    # Read the csv file
    with open(infile_name, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # read the data
            first_name = row[0]
            surname = row[1]
            email = row[2]
            mobile = row[3] if len(row) > 3 else ''
           
            full_name = first_name + " " + surname
            print full_name

            p, created = Person.objects.get_or_create(name=full_name)
            existing_mobile = p.mobile

            # update person details if necessary
            if not p.email:
                p.email = email
            elif p.email != email:
                update_notes(p, email)
                logfile.write('Check email of: ' + full_name + '\n')

            if not p.gender:
                p.gender = 't'
            
            if mobile:
                if existing_mobile:
                    update_notes(p, existing_mobile)
                    logfile.write('Check mobile of: ' + full_name + '\n')
                p.mobile = mobile 
            
            p.save()

            # create new participant
            new_participant = Participant()
            new_participant.person = p
            new_participant.workshop = ws
            new_participant.institution = temp_institute # temp value that needs to be updated manually
            new_participant.role = 't' # temp value
            new_participant.career_stage = '13' # temp value
            new_participant.offer = True
            new_participant.acceptance = True

            new_participant.save()                


if __name__ == '__main__':

    extra_info="""
example:
  $ python manage.py shell
  >>> import subprocess
  >>> subprocess.call(['utils/importer.py', 'participant_data.csv', '10']) 

input file format:
  Four columns are expected: first name, surname, email, mobile  

"""

    description = 'Import participant data from a csv file for a single workshop.'
    parser = argparse.ArgumentParser(description=description,
                                     epilog=extra_info, 
                                     argument_default=argparse.SUPPRESS,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("infile", type=str, help="Input file name")
    parser.add_argument("workshop_index", type=int, help="Database index of the workshop")

    args = parser.parse_args()

    main(args.infile, args.workshop_index)

