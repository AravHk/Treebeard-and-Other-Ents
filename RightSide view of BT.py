# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append((root,0,0))

        row_map = defaultdict(list)

        while queue:
            m , column , row = queue.popleft()
            if not row_map[row]:
                row_map[row].append(m.val)
            else:
                row_map[row] = [m.val]
            
            if m.left:
                queue.append((m.left,column-1,row+1))
            if m.right:
                queue.append((m.right,column+1,row+1))
        
        ans = []
        for momo in sorted(row_map.keys()):
            ans.extend(row_map[momo])
        return ans
