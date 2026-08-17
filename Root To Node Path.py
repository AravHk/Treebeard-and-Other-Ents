"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def paths(self, root,target):
        # code here
        result = []
        if root==None:
          return False
          
        result.append(root.data)
        
        if root.data == target:
          return True
        if self.paths(node.left,target) or self.paths(node.right,target):
          return True

        result.pop()
        return False
    def solve(self,root,b):
      arr = []
      if root==None:
        return arr
      self.paths(arr,b)
      return arr
