"No helper function is used"
"Very similar to preorder traversal with two differences"
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
def levelOrder(root,result):
    if root is None:
        return result
    q=[]
    q.append(root)
    while q:
        node = q.pop(0)
        result.append(node.data)
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
    return result

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.right = Node(100)
print(levelOrder(root,[]))