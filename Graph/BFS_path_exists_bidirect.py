#Not the complete answer
print("Final Solution")
from collections import defaultdict
class Graph: #adjacency list rep
    def bfs_iterative(self,edges,source,dest):
        # if source is None or source not in graph:
        #     return "invalid input"
        graph = self.makeAdjList(edges)
        visited = set()
        stack = [source]

        while(stack):
            s = stack.pop()
            if s == dest: return True
            ############
            if s not in visited:
                visited.add(s)
            ############
            print("stack: ",stack)
            for neighbor in graph[s]:
                if neighbor not in visited:
                    stack.insert(0,neighbor)
                # stack.append(neighbor) # maybe I might have to change it to stack.insert(0,neighbor)
        return False
    def makeAdjList(self,edges): # ex: [ [0,1], [0,2], [0,3], [1,2], [2,4] ] ==> {0:[1,2,3], 1:[2], 2:[4]}
        d = defaultdict(list)
        for elem in edges:
            d[elem[0]].append(elem[1])
            d[elem[1]].append(elem[0])
        return d
print("bi-directional rep: ",Graph().makeAdjList([ [0,1], [0,2], [0,3], [1,2], [2,4] ]))
print(Graph().bfs_iterative([ [0,1], [0,2], [0,3], [1,2], [2,4] ],0,4))

print("bi-directional rep: ",Graph().makeAdjList([[0,1],[0,2],[3,5],[5,4],[4,3]]))
print(Graph().bfs_iterative([[0,1],[0,2],[3,5],[5,4],[4,3]],0,4))
