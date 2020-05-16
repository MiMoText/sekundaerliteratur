import ontospy
from ontospy.ontodocs.viz.viz_html_single import *

g = ontospy.Ontospy("C:/Users/Administrator/PycharmProjects/mimotext/bibliographie.rdf")

v = HTMLVisualizer(g) # => instantiate the visualization object
v.build() # => render visualization. You can pass an 'output_path' parameter too
v.preview() # => open in browser
