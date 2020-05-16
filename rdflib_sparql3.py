import rdflib
from rdflib.namespace import RDF
from rdflib.namespace import DCTERMS
from rdflib.namespace import OWL
from rdflib.namespace import Namespace
import pprint
import rdflib_jsonld
from rdflib import plugins
from rdflib import query
import rdflib.plugins.sparql.results.csvresults as csvresults

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
    SELECT DISTINCT ?au ?ti ?key
    WHERE{
        ?exp dcterms:creator ?au.
        ?exp dcterms:title ?ti.
        ?man prism:keyword ?key.
        
        

    }
    LIMIT 100
    """)

result = g.serialize()

for i in range(5):
    print(i)
    print("\n")
    print(result)
