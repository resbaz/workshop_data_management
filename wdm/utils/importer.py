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
    logfile = open('import.log', 'w')

    # Create a dict of all the persons in the database    
    person_list = {}
    people = Person.objects.all()
    for person in people:
        person_list[person.name] = {'id': person.id, 'Name': person.name, 'email': person.email}

    # Create a temporary institute entry that will be updated manually later
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

            if full_name in person_list.keys():
                temp_person = Person.objects.get(id=person_list[full_name]['id'])
                
                # update person details if necessary
                existing_email = temp_person.email
                existing_mobile = temp_person.mobile
                if existing_email != email:
                    update_notes(temp_person, email)
                    logfile.write('Check email of: ' + full_name + '\n')
                if mobile:
                    if existing_mobile:
                        update_notes(temp_person, existing_mobile)
                        logfile.write('Check mobile of: ' + full_name + '\n')
                    temp_person.mobile = mobile 
                    temp_person.save()

                # create new participant
                new_participant = Participant()
                new_participant.person = temp_person
                new_participant.workshop = ws
                new_participant.institution = temp_institute # temp value that needs to be updated manually
                new_participant.role = 't' # temp value
                new_participant.career_stage = '13' # temp value
                new_participant.offer = True
                new_participant.acceptance = True

                new_participant.save()                

            else:
                logfile.write('No person entry for this participant: ' + full_name + '\n')


if __name__ == '__main__':

    extra_info="""
example:
  $ python importer participant_data.csv 10

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

