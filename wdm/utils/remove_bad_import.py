Another python/django script, to be run from the shell.

ws = Workshop.objects.get(id=43); parts = ws.participants.all(); 
for part in parts: person = part.person; part.delete(); person.delete()
