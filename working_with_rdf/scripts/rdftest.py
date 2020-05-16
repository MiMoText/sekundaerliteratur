import urllib3
import rdflib
import rdflib_jsonld

with open("../data_in/bibliographie.rdf", encoding="utf-8") as f:
    rdf_triple_data = f.read()

# Leeren Graph anlegen in den wir die Daten später laden können
graph = rdflib.Graph()

graph.parse(data=rdf_triple_data, format="xml")

new_data = graph.serialize(format="nt")
print(new_data)

predicate_query = graph.query("""
                     select ?predicates
                     where {?s ?predicates ?o}
                     """)

# For each results print the value
for row in predicate_query:
    print('%s' % row)

# TODO Beispielabfrage vorbereiten
# s. https://www.oclc.org/developer/news/2016/making-sense-of-linked-data-with-python.en.html
# für fortgeschrittene Umsetzung

