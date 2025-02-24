# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return ans
        
        queue = deque([root])
        while queue:
            cur_len = len(queue)
            row_max = float("-inf")

            for _ in range(cur_len):
                node = queue.popleft()
                row_max = max(row_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(row_max)
                
        return ans