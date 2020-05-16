import graphviz
from graphviz import Graph
import rdflib
from rdflib import tools
from rdflib.tools import rdf2dot
from rdflib import Graph
import pprint
from rdflib import URIRef
from rdflib.namespace import RDF
from rdflib.namespace import DC
from rdflib.namespace import OWL

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




