import rdflib
import sqlite3



from rdflib.graph import ConjunctiveGraph
g = ConjunctiveGraph()

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
    LIMIT 1
    """)

# for triple in g:
    # print(triple)

outfile = open("test.txt", "w")
output = str(qres.serialize(format="n3"))
outfile.writelines(output)

outfile.write(output)


print("type output", type(output))

print("laenge output", len(output))
print(output[0:776])

"""
graph = rdflib.Graph(store="Sleepycat", identifier="mygraph")
# first time create the store
graph.open("myRDFLibStore", create=True)

# work with the graph
graph.add(qres)

# when done
graph.close()
"""

