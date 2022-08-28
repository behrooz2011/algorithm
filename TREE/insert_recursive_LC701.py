''' 
https://leetcode.com/problems/insert-into-a-binary-search-tree/

You are given the root node of a binary search tree (BST) and a value to 
insert into the tree. 
Return the root node of the BST after the insertion. 
It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion,
 as long as the tree remains a BST after insertion. You can return any of them.
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        if root is None:
            return Node(val)

        if val > root.data: # if new value is greater than the node, shift right

            if not root.right:
                root.right = Node(val)
            else:
                self.insertIntoBST(root.right,val)

        else:

            if not root.left:
                root.left = Node(val)
            else:
                self.insertIntoBST(root.left,val)
        

class Inorder:
    def inOrderRecur(self,root, result):
        if not root:
            return result
        self.inOrderRecur(root.left,result)
        result.append(root.data)
        self.inOrderRecur(root.right,result)
        return result

r=Node(1)
r.right = Node(3)
r.left= Node(2)
r.left.left=Node(4)
r.left.right = Node(5)
r.right.right = Node(7)
r.right.left= Node(6)


# Solution().insertIntoBST(r,)
print("Inorder BEFORE inserting 2.5 :",Inorder().inOrderRecur(r,[]))
Solution().insertIntoBST(r,2.5)
print("Inorder AFTER inserting 2.5 :",Inorder().inOrderRecur(r,[]))

print(" \n___________________________________________")

t =  Node(4)
t.left = Node(2)
t.left.left = Node(1)
t.left.right = Node(3)

t.right = Node(6)
t.right.left = Node(5)
t.right.right = Node(7)

print("Inorder BEFORE inserting 2.5 :",Inorder().inOrderRecur(t,[]))
Solution().insertIntoBST(t,2.5)
print("Inorder AFTER inserting 2.5 :",Inorder().inOrderRecur(t,[]))