#Not the complete answer
print("start")
from collections import defaultdict
class Graph: #adjacency list rep
    # def __init__(self,gdict=None):
    #   if gdict is None:
    #      gdict = {}
    #   self.gdict = gdict
    def bfs_iterative(self,edges,source):
        # if source is None or source not in graph:
        #     return "invalid input"
        graph = self.makeAdjList(edges)
        path = [] #visited
        stack = [source]

        while(stack):
            s = stack.pop()
            if s not in path:
                path.append(s)
            if s not in graph: # if s is a leaf
                continue
            for neighbor in graph[s]:
                stack.insert(0,neighbor)
                # stack.append(neighbor) # maybe I might have to change it to stack.insert(0,neighbor)
        return path
    def makeAdjList(self,edges): # ex: [ [0,1], [0,2], [0,3], [1,2], [2,4] ] ==> {0:[1,2,3], 1:[2], 2:[4]}
        d = defaultdict(list)
        for elem in edges:
            d[elem[0]].append(elem[1])
        return d

    def pathExists(self,edges,source,dest):
        graph = self.makeAdjList(edges)
print(Graph().makeAdjList([ [0,1], [0,2], [0,3], [1,2], [2,4] ]))
print(Graph().bfs_iterative( [ [0,1], [0,2], [0,3], [1,2], [2,4] ], 0))
print("\n")

print(Graph().makeAdjList([[0,1],[0,2],[3,5],[5,4],[4,3]]))
print(Graph().bfs_iterative( [[0,1],[0,2],[3,5],[5,4],[4,3]], 0))

print("\n")
print(Graph().makeAdjList([[0,1],[0,2],[2,3],[3,5],[5,4],[4,3]]))
print(Graph().bfs_iterative( [[0,1],[0,2],[2,3],[3,5],[5,4],[4,3]], 0))