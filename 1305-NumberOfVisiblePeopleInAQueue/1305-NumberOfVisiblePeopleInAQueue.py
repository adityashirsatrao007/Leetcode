# Last updated: 6/4/2025, 9:20:55 PM
class Solution(object):
    def canSeePersonsCount(self, heights):
        """
        :type heights: List[int]
        :rtype: List[int]
        """
        n = len(heights)
        answer = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and heights[i] > heights[stack[-1]]:
                stack.pop()
                answer[i] += 1
            if stack:
                answer[i] += 1
            stack.append(i)

        return answer
