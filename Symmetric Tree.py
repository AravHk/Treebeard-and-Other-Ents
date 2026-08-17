'''# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        inorder1 = []
        inorder2=[]
        self.helper(root.left,inorder1)
        self.helper(root.right,inorder2)
        return inorder1==inorder2[::-1]
    def helper(self,root,inorder):
        if not root:
            return []
        self.helper(root.left,inorder)
        inorder.append(root.val)
        self.helper(root.right,inorder)
196/201 testcases
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root==None or self.helper(root.left,root.right)
    def helper(self,root1,root2):
        if root1==None or root2==None:
            return root1==root2
        if root1.val != root2.val:
            return False
        return self.helper(root1.left , root2.right) and self.helper(root1.right , root2.left)

