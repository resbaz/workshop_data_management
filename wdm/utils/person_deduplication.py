'''
Person deduplication
TODO: make an actual script
currently: run this within the django shell
I prefer shell_plus personally.
./manage shell_plus

Obviously this can be performed at any time,
generally it's run after an import or bunch
of imports in order to trim as we go.

'''

from difflib import get_close_matches

people = Person.objects.values_list('name', flat=True)

ws = Workshop.objects.get(id=43)
participants = ws.participants.values_list('name', flat=True)

for participant in participants:
    dupes = get_close_matches(participant, people, 2, 0.7)    
    if len(dupes) > 1:
        print dupes

'''
You should see the following output, then run the transfer:

[u'Elizabeth Bowman', u'Elizabeth Lowe']
[u'Elizabeth Read', u'Elizabeth Lowe']
[u'Giulia Gerboni', u'Giulia gerboni'] # Person id's 836 and 765
[u'Lina Wang', u'Li Yang']
[u'Peter Yoo', u'Peter Keov']
[u'Philipp Nauer', u'Philip Sumner']
[u'Song Cheng', u'Long Chen']
[u'Sou Mehdikhani', u'Mahboobeh Mehdikhani']
[u'Yu Bai', u'Ying Bai']
>>> p1 = Person.objects.get(id=765)
>>> p2 = Person.objects.get(id=836)
>>> p2.participations.all()
[<Participant: 2015-06-08: MATLAB, Giulia Gerboni>]
>>> part = p2.participations.all()
>>> for p in part:
...    p.person
... 
<Person: Giulia Gerboni>
>>> for p in part:
...    p.person = p1
...    p.save()
... 
>>> p2.participations.all()
[]
>>> p2.delete()

