'''
                 1
               / | \
              /  |  \
            2    3   4
           / \       /\
          /   \     /  \
         5     6   7    8
        / \   /    /\
       /   \ /    /  \
      9     10    11  12

graph = {
    1 : [2, 3, 4],
    2 : [5, 6],
    4 : [7,8],
    5 : [9, 10],
    6 : [10]
    7 : [11, 12]   
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
            print("stack: ",stack)
            s = stack.pop()
            if s not in path:
                path.append(s)
            if s not in graph: # if s is a leaf
                continue
            for neighbor in graph[s]:
                #########################
                # check if there's a cycle, ie a repetitive vertex
                if neighbor in stack:
                    return True
                #########################
                stack.insert(0,neighbor)
                # stack.append(neighbor) # maybe I might have to change it to stack.insert(0,neighbor)
        # return path
        return False # ie, there's no repetitive value in stack so ,no cycle either

graph = {
    1 : [2, 3, 4],
    2 : [5, 6],
    4 : [7,8],
    5 : [9, 10],
    6 : [10],
    7 : [11, 12]   
}
g = Graph()
print(g.bfs_iterative(graph,1))



graph_new = {
    "A" : ["B", "C", "D"],
    "B" : ["E"],
    "C" : ["F", "G"],
    "D" : ["H"],
    "E" : ["I"],
    "F" : ["J"],
    "H": ["J"]
}
graph3 = {0:[1, 2, 3], 1:[2], 2:[4]}
print(g.bfs_iterative(graph3,0))
print(g.bfs_iterative(graph_new,"A"))

graph4 = {
    "A" : ["B", "C", "D"],
    "B" : ["E"],
    "C" : ["F", "G"],
    "D" : ["H"],
    "E" : ["I"],
    "F" : ["J"],

}
print(g.bfs_iterative(graph4,"A"))