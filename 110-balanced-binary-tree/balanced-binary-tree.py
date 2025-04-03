# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode):
        def height(node):
            if not node:
                return 0
            
            left_height = height(node.left)
            if left_height == -1:
                return -1

            right_height = height(node.right)
            if right_height == -1:
                return -1

            if abs(left_height - right_height) >= 2:
                return -1

            return max(left_height, right_height) + 1
        height = height(root)
        if height == -1:
            return False
        return True