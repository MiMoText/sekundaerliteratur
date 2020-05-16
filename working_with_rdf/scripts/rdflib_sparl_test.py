import rdflib
import rdflib.plugins
import rdflib.plugins.sparql
import rdflib.plugins.sparql.results.csvresults as csvresults


g = rdflib.graph.Graph()
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
    SELECT DISTINCT ?au ?ti ?key ?vial
    WHERE{
        ?exp dcterms:creator ?au.
        ?exp dcterms:title ?ti.
        ?man prism:keyword ?key.
        ?s dcterms:creator ?viaf.
        

    }
    """)

print("Abfrage erledigt")

csvdata = csvresults.CSVResultSerializer(qres)
print(csvdata)



