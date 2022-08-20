#Left Data Right
#LDR
print("hi")
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right =None


def inOrderIter(root, result):
    if not root:
        return result
    stack =[]
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            result.append(node.data)
            node = node.right


def inorderTraversal(root):
    answer = []
    inOrderIter(root, answer)
    return answer

r=Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)
r.right.right = Node(7)
r.right.left= Node(6)

def automaticTreeCreation(nodeNumber):
    r
    for i in range(1,nodeNumber +1):
        if not r.data:
            r= Node(i)
        if i != 1 and i%2 == 0:
            r.left = Node(i)
            r= 
        if i != 1 and i%2 == 1:
            r.right = Node(i)
            r = r.right


print("InOrder Traversal Iterative: ",inorderTraversal(r))