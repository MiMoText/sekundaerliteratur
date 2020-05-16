import rdflib

g = rdflib.Graph()
g.parse("bibliographie.rdf")

qres = g.query(
    """ SELECT
    """

)