from rdflib import Graph
import pprint
from rdflib import URIRef
import rdflib_jsonld
import rdflib

g = Graph()
g.parse("bibliographie.rdf", format="xml")
print(len(g))


# Ausgabe der Triple
# verständliche Beispieltriple s. Doku S. 7
for stmt in g:
    pprint.pprint(stmt)

eintrag = URIRef("http://www.kompetenzzentrum.uni-trier.de/bgrf/8714Expression")
if (eintrag, None, None) in g:
    print("This graph contains triples about eintrag")
else: print("no content found")

print(eintrag)

print("Hier kommen Prädikate")
predicates = g.predicates(subject=None, object=None)
# For each item in the predicates generator, print it out
for predicate in predicates:
    print(predicate)

print("Hier kommen Objekte")
objects = g.objects(subject=None, predicate=None)
for object in objects:
    print(object)

print("Hier kommen Subjekte")
subjects = g.subjects(object=None, predicate=None)
for subject in subjects:
    print(subject)


