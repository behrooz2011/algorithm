from collections import defaultdict
d = defaultdict(lambda:0)
# print(d["A"])


class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right =None


def preOrderRecur(root, result):
    if not root:
        return result
    result.append(root.data)
    preOrderRecur(root.left,result)
    preOrderRecur(root.right,result)
    return result
    # preorderRecursive(root.right, result)
#No need for this one below
def preorderTraversal(root):
    answer = []
    preOrderRecur(root, answer)
    return answer

r=Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)
r.right.right = Node(7)
r.right.left= Node(6)

print(preOrderRecur(r,[]))
# print("this is the result: ",preorderTraversal(r))
"""this is the result:  [1, 2, 4, 5, 3, 6, 7]"""
