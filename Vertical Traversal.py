# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append((root,0,0))
        # vert level
        col_map = defaultdict(list)

        while queue:
            m , j , k = queue.popleft()
            col_map[j].append((k,m.val))

            if m.left:
                queue.append((m.left,j-1,k+1))
            if m.right:
                queue.append((m.right,j+1,k+1))
        
        ans = []
        for momo in sorted(col_map.keys()):
            col_map[momo].sort(key = lambda x:(x[0],x[1]))

            ans.append([val for row,val in col_map[momo]])
        return ans
