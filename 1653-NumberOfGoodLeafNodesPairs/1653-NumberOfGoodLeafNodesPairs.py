# Last updated: 6/4/2025, 9:20:06 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        def dfs(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [1]
            
            left_dists = dfs(node.left)
            right_dists = dfs(node.right)
            
            for l in left_dists:
                for r in right_dists:
                    if l + r <= distance:
                        count[0] += 1
            
            return [d + 1 for d in left_dists + right_dists]
        
        count = [0]
        dfs(root)
        return count[0]
