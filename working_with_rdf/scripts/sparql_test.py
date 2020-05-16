from rdflib import Graph

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