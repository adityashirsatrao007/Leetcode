# Last updated: 6/4/2025, 9:19:08 PM
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def getDirections(self, root, startValue, destValue):
        """
        :type root: Optional[TreeNode]
        :type startValue: int
        :type destValue: int
        :rtype: str
        """
        
        # Helper function to find the Lowest Common Ancestor (LCA)
        def findLCA(root, p, q):
            if not root or root.val == p or root.val == q:
                return root
            left = findLCA(root.left, p, q)
            right = findLCA(root.right, p, q)
            if left and right:
                return root
            return left if left else right
        
        # Helper function to find the path from a given node to the target value
        def findPath(root, target, path):
            if not root:
                return False
            if root.val == target:
                return True
            path.append('L')
            if findPath(root.left, target, path):
                return True
            path.pop()
            path.append('R')
            if findPath(root.right, target, path):
                return True
            path.pop()
            return False
        
        # Find the LCA of startValue and destValue
        lca = findLCA(root, startValue, destValue)
        
        # Find the path from LCA to startValue
        pathToStart = []
        findPath(lca, startValue, pathToStart)
        
        # Find the path from LCA to destValue
        pathToDest = []
        findPath(lca, destValue, pathToDest)
        
        # Convert pathToStart to 'U' steps
        stepsToStart = 'U' * len(pathToStart)
        
        # Combine stepsToStart and pathToDest to get the final directions
        return stepsToStart + ''.join(pathToDest)

# Example usage
root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(4)

startValue = 3
destValue = 6

solution = Solution()
print(solution.getDirections(root, startValue, destValue))  # Output: "UURL"
