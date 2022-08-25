# from collections import defaultdict

# from pkg_resources import ResolutionError
# d = defaultdict(lambda:0)
# # print(d["A"])

print("hi")
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right =None

class Solution:
    def inOrderRecur(self,root, result):
        if not root:
            return result
        self.inOrderRecur(root.left,result)
        result.append(root.data)
        self.inOrderRecur(root.right,result)
        return result

# def inorderTraversal(root):
#     answer = []
#     inOrderRecur(root, answer)
#     return answer

r=Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)
r.right.right = Node(7)
r.right.left= Node(6)
r.left.right.right = Node(99)
r.left.left.left = Node(8)

# print( "InOrder Traversal Recursively:",inorderTraversal(r))
print( " CLASS/ InOrder Traversal Recursively:",Solution().inOrderRecur(r,[]))