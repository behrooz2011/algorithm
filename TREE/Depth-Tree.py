from collections import defaultdict
d = defaultdict(lambda:0)
# print(d["A"])

class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right =None
class Solution:
    # def __init__(self,i):
    #     self.i = 1
    def ino(self, root, result):
        i=0
        if not root:
            return
        if root.left or root.right:
            d[i] += 1
            i += 1
        self.ino(root.left,result)
        result.append(root.data)
        self.ino(root.right,result)
        print("this is i:\t",i)
        print("this is d:\t",d)
        return(result)
r=Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)
r.left.left.right = Node(50)
r.left.left.right.left = Node(500)
print(Solution().ino(r,[]))
"""Finding the depth of a tree"""