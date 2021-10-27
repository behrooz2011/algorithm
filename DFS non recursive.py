# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
def dfs_non_recursive(graph, source):

       if source is None or source not in graph:

           return "Invalid input"

       path = []

       stack = [source]

       while(len(stack) != 0):

           s = stack.pop()

           if s not in path:

               path.append(s)

           if s not in graph:

               #leaf node
               continue

           for neighbor in graph[s]:

               stack.append(neighbor)

       return " ".join(path)
graph = {"A":["D","C","B"],
   "B":["E"],
   "C":["G","F"],
   "D":["H"],
   "E":["I"],
   "F":["J"]}
print(dfs_non_recursive(graph,"E"))
print(dfs_non_recursive(graph,"C"))
print(dfs_non_recursive(graph,"A"))
print(dfs_non_recursive(graph,"B"))
#image: https://likegeeks.com/wp-content/uploads/2020/06/03_implementing_dfs_in_python_01.jpg
