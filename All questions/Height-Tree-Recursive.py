#"hight of a tree - recursive"
class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
        
def h(root):
    m=0
    if root is None:
        return(0)
    if root.left is not None:
       m = max(m,1+h(root.left))
    if root.right is not None:
        m= max(m,1+h(root.right))
    return(m)
root = Node(1)
root.left=Node(2)
root.right = Node(10)
root.right.right = Node(100)
root.right.right.left = Node(12)
root.right.right.left.right = Node(120)

print(h(root))
#res: 4