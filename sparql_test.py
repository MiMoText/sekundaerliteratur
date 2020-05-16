from rdflib import Graph
import pprint
from rdflib import URIRef
import rdflib_jsonld
import rdflib
import rdflib_sparql

g = Graph()
g.parse("bibliographie.rdf", format="xml")
print(len(g))


qres = g.query(
    """ SELECT ?eintraege
    WHERE{
    ?eintraege dcterms:creator ?au.
    }
    """
)