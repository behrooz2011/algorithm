#Depth First Search: Recursive
#image: https://likegeeks.com/wp-content/uploads/2020/06/03_implementing_dfs_in_python_01.jpg

graph = {"A":["D","C","B"],
   "B":["E"],
   "C":["G","F"],
   "D":["H"],
   "E":["I"],
   "F":["J"]
}

def recursive_dfs(graph, source,path = []):

       if source not in path:

           path.append(source)

           if source not in graph:
               # leaf node, backtrack
               return path

           for neighbour in graph[source]:

               path = recursive_dfs(graph, neighbour, path)


       return " ".join(path)
# print(recursive_dfs(graph,"E"))
# print(recursive_dfs(graph,"C"))
# print(recursive_dfs(graph,"A"))
print(recursive_dfs(graph,"B"))