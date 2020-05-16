import rdflib
from rdflib.namespace import RDF
from rdflib.namespace import DCTERMS
from rdflib.namespace import OWL
from rdflib.namespace import Namespace
import pprint
import rdflib_jsonld
from rdflib import plugins
from rdflib import query


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
SELECT DISTINCT *
WHERE{
   
    ?entry prism:keyword ?key. 
    
   
  
}
ORDER BY ?id
""")

for row in qres:
    pprint.pprint(row)
print(type(row))

print(type(qres))




#s = g.serialize()
#print(type(s))

#with open("keywords.txt", "w", "utf-8") as file:
    #file.writelines(s)

#c = g.all_nodes()
#print(c)
