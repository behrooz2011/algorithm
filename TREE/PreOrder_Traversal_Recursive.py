from collections import defaultdict
d = defaultdict(lambda:0)
# print(d["A"])

print("hi")
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
    # preorderRecursive(root.right, result)

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

preOrderRecur(r,[])
print("this is the result: ",preorderTraversal(r))
