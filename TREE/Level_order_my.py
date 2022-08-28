# from logging import root


class Node:
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
class Level:
    def level(self,root,result=[]):
        if root is None:
            return
        helper = []
        node = root
        print("root: ",root.data)
        result.append(node.data)
        while helper or node: # or while len(helper) > 0
            if node.left:
                result.append(node.left.data)
                helper.insert(0,node.left)
            if node.right:
                result.append(node.right.data)
                helper.insert(0,node.right)
            # print("this is helper", helper)
            if len(helper) != 0:
                node = helper.pop()
            else:
                break
        return result

        ''' Clean Solution'''
    def levelOrder(self,root, result):
        if root is None:
            return 
        queue = [] 
        queue.append(root)
        result.append(root.data)

        while queue:
            node = queue.pop()
            if node.left:
                result.append(node.left.data)
                queue.insert(0,node.left)
            if node.right:
                result.append(node.right.data)
                queue.insert(0,node.right)
        return result
r = Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)

r.right.right = Node('Null')
r.right.left = Node(50)

print(Level().level(r,[]))


