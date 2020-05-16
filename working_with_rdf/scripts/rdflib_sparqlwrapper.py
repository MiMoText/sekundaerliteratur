import rdflib
from SPARQLWrapper import SPARQLWrapper

g = rdflib.Graph()
g.parse("bibliographie.rdf")


qres = g.query(
    """
    PREFIX loc: <http://www.w3.org/2007/uwa/context/location.owl#>
    PREFIX dct: <http://purl.org/dc/terms/>
    PREFIX dcterms: <http://purl.org/dc/terms/>
    PREFIX fabio: <http://purl.org/spar/fabio/>
    PREFIX co: <http://purl.org/ontology/co/core#>
    PREFIX biro: <http://purl.org/spar/biro/>
    PREFIX frbr: <http://purl.org/vocab/frbr/core#>
    PREFIX prism: <http://prismstandard.org/namespaces/basic/2.0/>
    SELECT DISTINCT ?au ?ti ?key ?viaf
    WHERE{
        ?exp dcterms:creator ?au.
        ?exp dcterms:title ?ti.
        ?man prism:keyword ?key.
        ?s dcterms:creator ?viaf.


    }
LIMIT 10
    """)


qres_serialized = qres.serialize(qres)
print(qres_serialized)