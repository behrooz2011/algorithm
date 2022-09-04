'''
                 A
               / | \
              /  |  \
            B    C    D
            |   / \    \
            E  F   G    H
            |  |   
            I  J

graph = {
    "A" : ["B", "C", "D"],
    "B" : ["E"],
    "C" : ["F", "G"],
    "D" : ["H"],
    "E" : ["I"],
    "F" : ["J]
}

'''
#BFS ironically!
class Graph: #adjacency list rep
    # def __init__(self,gdict=None):
    #   if gdict is None:
    #      gdict = {}
    #   self.gdict = gdict
    def bfs_iterative(self,graph,source):
        if source is None or source not in graph:
            return "invalid input"
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
graph1 = {
    "A" : ["B", "C", "D"],
    "B" : ["E"],
    "C" : ["F", "G"],
    "D" : ["H"],
    "E" : ["I"],
    "F" : ["J"]
}
g = Graph()
print(g.bfs_iterative(graph1,"A"))
""" BFS result: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] """


graph2 = {
    "A" : ["B", "C", "D"],
    "B" : ["E"],
    "C" : ["F", "G"],
    "D" : ["H"],
    "E" : ["I"],
    "F" : ["J"],
    "J": ["H"]
}
graph3 = {0:[1, 2, 3], 1:[2], 2:[4]}
print(g.bfs_iterative(graph3,0))