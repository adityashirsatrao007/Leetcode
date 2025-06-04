# Last updated: 6/4/2025, 9:17:44 PM
class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        dp = [[0 for _ in range(k + 1)] for _ in range(n)]
        maxi = [[0 for _ in range(k + 1)] for _ in range(n)]
        mp = {}

        for i in range(n):
            for j in range(k + 1):
                if i == 0:
                    dp[i][j] = 1
                    maxi[i][j] = max(maxi[i][j], dp[i][j])
                elif j == 0:
                    dp[i][j] = 1
                    t = mp.get(nums[i], -1)
                    if t != -1:
                        dp[i][j] = max(dp[i][j], dp[t][j] + 1)
                else:
                    dp[i][j] = maxi[i - 1][j - 1] + 1
                    t = mp.get(nums[i], -1)
                    if t != -1:
                        dp[i][j] = max(dp[i][j], dp[t][j] + 1)
                maxi[i][j] = max(dp[i][j], maxi[i - 1][j])
            mp[nums[i]] = i

        return max(dp[n - 1][k], maxi[n - 1][k])
