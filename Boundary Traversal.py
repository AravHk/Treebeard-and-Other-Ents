'''
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def isLeaf(self,root):
        return root.left is None and root.right is None
    def addLeftBoundary(self,root,ans):
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                ans.append(curr.data)
            if curr.left != None:
                curr = curr.left
            else:
                curr= curr.right
    def addRightBoundary(self,root,ans):
        curr=root.right
        while curr:
            if not self.isLeaf(curr):
                ans.append(curr.data)
            if curr.right!=None:
                curr = curr.right
            else:
                curr = curr.left
    def addLeaves(self,root,ans):
        if root is None:
            return
        if self.isLeaf(root):
            ans.append(root.data)
            return
        self.addLeaves(root.left,ans)
        self.addLeaves(root.right,ans)
    def boundaryTraversal(self, root):
        # code here
        if root is None:
            return []
        if self.isLeaf(root):
            return [root.data]
        ans = []
        ans.append(root.data)
        
        self.addLeftBoundary(root,ans)
        self.addLeaves(root,ans)
        self.addRightBoundary(root,ans)
        
        return ans
        
