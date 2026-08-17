"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
In case , you want all nodes instead of leaf node alone remove the if condn before the result.append stmt.
"""
from collections import deque
class Solution:
    def paths(self, root):
        # code here
        result = []
        def dfs(node , path):
            if not node:
                return
            path.append(node.data)
            if not node.left and not node.right:
                result.append(path[:])
            
            dfs(node.left,path)
            dfs(node.right,path)
            
            path.pop()
        
        dfs(root,[])
        return result
