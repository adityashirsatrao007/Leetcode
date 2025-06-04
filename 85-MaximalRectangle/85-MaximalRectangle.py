# Last updated: 6/4/2025, 9:23:19 PM
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        def largestRectangleArea(heights):
            stack = [-1]
            max_area = 0
            for i in range(len(heights)):
                while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                    height = heights[stack.pop()]
                    width = i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
            while stack[-1] != -1:
                height = heights[stack.pop()]
                width = len(heights) - stack[-1] - 1
                max_area = max(max_area, height * width)
            return max_area

        max_area = 0
        dp = [0] * len(matrix[0])
        
        for row in matrix:
            for j in range(len(row)):
                dp[j] = dp[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, largestRectangleArea(dp))
        
        return max_area
