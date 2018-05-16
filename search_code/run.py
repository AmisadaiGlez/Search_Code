# Search methods
from operator import itemgetter, attrgetter, methodcaller

import search

ab = search.GPSProblem('A', 'B', search.romania)
ap = search.GPSProblem('A', 'P', search.romania)
ag = search.GPSProblem('A', 'G', search.romania)
av = search.GPSProblem('A', 'V', search.romania)
ad = search.GPSProblem('A', 'D', search.romania)

#print search.breadth_first_graph_search(ab).path()
#print search.depth_first_graph_search(ab).path()


print search.ra_graph_search(ab).path()
print "Numero de nodos expandidos con RA de AB: ", search.expand, "\n"
search.expand = 0
print search.ras_graph_search(ab).path()
print "Numero de nodos expandidos con RAS de AB: ", search.expand, "\n"
search.expand = 0

print search.ra_graph_search(ap).path()
print "Numero de nodos expandidos con RA de AP: ", search.expand, "\n"
search.expand = 0
print search.ras_graph_search(ap).path()
print "Numero de nodos expandidos con RAS de AP: ", search.expand, "\n"
search.expand = 0

print search.ra_graph_search(ag).path()
print "Numero de nodos expandidos con RA de AG: ", search.expand, "\n"
search.expand = 0
print search.ras_graph_search(ag).path()
print "Numero de nodos expandidos con RAS de AG: ", search.expand, "\n"
search.expand = 0

print search.ra_graph_search(av).path()
print "Numero de nodos expandidos con RA de AV: ", search.expand, "\n"
search.expand = 0
print search.ras_graph_search(av).path()
print "Numero de nodos expandidos con RAS de AV: ", search.expand, "\n"
search.expand = 0

print search.ra_graph_search(ad).path()
print "Numero de nodos expandidos con RA de AD: ", search.expand, "\n"
search.expand = 0
print search.ras_graph_search(ad).path()
print "Numero de nodos expandidos con RAS de AD: ", search.expand, "\n"
search.expand = 0


#print ab.h(search.Node(ab.initial))


#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
