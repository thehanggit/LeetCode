# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []
        
        # q = deque([root])
        # temp = deque()
        # levels = [[root.val]]

        # while q:
        #     node = q.popleft()
        #     if node.left:
        #         temp.append(node.left)
        #     if node.right:
        #         temp.append(node.right)
        #     if not q:
        #         if temp:
        #             levels.append([n.val for n in temp])
        #             q = temp
        #             temp = deque()
        # return levels

        if not root:
            return []

        queue = deque([root])
        res = [[root.val]]
        while queue:
            curr = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    left = node.left
                    queue.append(left)
                    curr.append(left.val)
                if node.right:
                    right = node.right
                    queue.append(right)
                    curr.append(right.val)
            if curr == []:
                continue
            else:
                res.append(curr)
        return res                
                
