'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''
from collections import defaultdict

class Solution:
    def topView(self, root):
        # code here
        
        if not root:
            return []
            
        queue = deque()
        queue.append((root,0,0))
        col_map = defaultdict(list)
        
        while queue:
            m , column , row  = queue.popleft()
            if not col_map[column]:
                col_map[column].append(m.data)
                
            if m.left:
                queue.append((m.left,column-1,row+1))
            if m.right:
                queue.append((m.right,column+1,row+1))
        ans = []
        for momo in sorted(col_map.keys()):
            ans.extend(col_map[momo])
        return ans
