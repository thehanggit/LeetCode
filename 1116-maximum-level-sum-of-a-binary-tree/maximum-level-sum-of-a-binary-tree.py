# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # maximum = float("-inf")
        # level = 1
        # min_level = 1

        # q = deque([root])
        # while q:
        #     curr_sum = 0
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         curr_sum += node.val
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
            
        #     if maximum < curr_sum:
        #         min_level = level
        #         maximum = curr_sum

        maximum = float("-inf")
        level = 1
        queue = deque([root])
        while queue:
            curr_sum = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
            if curr_sum > maximum:
                min_level = level
                maximum = curr_sum
            level += 1
        
        return min_level

        
        

            
            

