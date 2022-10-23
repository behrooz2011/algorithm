
"""100. Same Tree
Easy
7.4K
156
Companies
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

 

Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        print("preQ: ",self.preQ(q,[]))
        print("preP: ",self.preP(p,[]))
        return (self.preQ(q,[]) == self.preP(p,[]))
        
    def preQ(self,q,result=[]):
        if q is None:
            result.append('null') # very important in order to not have similar results array representing different trees
            return
        result.append(q.val)
        self.preQ(q.left,result)
        self.preQ(q.right,result)
        return result
        
    def preP(self,p,result=[]):
        if p is None:
            result.append('null')
            return
        result.append(p.val)
        self.preP(p.left,result)
        self.preP(p.right,result)
        return result