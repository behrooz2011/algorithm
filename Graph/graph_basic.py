'''
Display graph vertices
Display graph edges
Add a vertex
Add an edge
Creating a graph

'''

'''
    a---b
    |   |
    c---d---e

    V = {a, b, c, d, e}
    E = {ab, ac, bd, cd, de}

    graph = { 
                "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
            }


'''

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """
"""                         Display Vertices                     """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """
class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = []
      self.gdict = gdict
# Get the keys of the dictionary
   def getVertices(self):
      return list(self.gdict.keys())
# Create the dictionary with graph elements
graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
print(g.getVertices())

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """
"""                         Display Edges                        """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """
class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict

   def edges(self):
      return self.findedges()
# Find the distinct list of edges
   def findedges(self):
      edgename = []
      for vrtx in self.gdict:
         for nxtvrtx in self.gdict[vrtx]:
            if {nxtvrtx, vrtx} not in edgename:
               edgename.append({vrtx, nxtvrtx})
      return edgename
# Create the dictionary with graph elements
graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
print(g.edges())

graph_elements_t = {  # with repetitive edges still the same answer
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e","b","c"],
   "e" : ["d"]
}
t = graph(graph_elements_t)
print(t.edges())

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """
"""                         Adding a vertex                        """
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""" """

class graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = {}
      self.gdict = gdict
   def getVertices(self):
      return list(self.gdict.keys())
# Add the vertex as a key
   def addVertex(self, vrtx):
      if vrtx not in self.gdict:
         self.gdict[vrtx] = []
# Create the dictionary with graph elements
graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}
g = graph(graph_elements)
g.addVertex("f")
print(g.getVertices())


