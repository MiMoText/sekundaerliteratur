import ontospy
from ontospy.ontodocs.viz.viz_html_single import *

g = ontospy.Ontospy("../working_with_rdf/data_in/bibliographie.rdf")

v = HTMLVisualizer(g) # => instantiate the visualization object
v.build() # => render visualization. You can pass an 'output_path' parameter too
v.preview() # => open in browser
