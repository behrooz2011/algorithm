from collections import defaultdict
#creates a dictionary with the default value of zero for each key
d = defaultdict(lambda:0)
# print('d["A"]: ',d["A"])
# print('d["A"]: ',d["B"])
# print('d["A"]: ',d["Z"])
# print('d: ',d)
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
        # print("this is i:\t",i)
        # print("this is d:\t",d)
        return(result)

print("d:",d)
""" Manual Creation of a Tree """
r=Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)
r.left.left.right = Node(50)
r.left.left.right.left = Node(500)
print(Solution().ino(r,[]))

rr=Node(1)
rr.right = Node(3)
rr.left= Node(2)
rr.left.left=Node(4)
rr.left.right = Node(5)
rr.right.left= Node(6)
rr.right.right = Node(7)
print(Solution().ino(rr,[]))
"""End of Manual Creation of a Tree"""


