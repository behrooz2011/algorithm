# from collections import defaultdict
# d = defaultdict(lambda:0)
# # print(d["A"])

#Pre and POST start with D
#DLR
print("hi")
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right =None


def preOrderIter(root, result):
    if not root:
        return result
    stack =[]
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.data)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    # preorderRecursive(root.right, result)

def preorderTraversal(root):
    answer = []
    preOrderIter(root, answer)
    return answer

r=Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)
r.right.right = Node(7)
r.right.left= Node(6)

print("PreOrder Traversal Iterative: ",preorderTraversal(r))