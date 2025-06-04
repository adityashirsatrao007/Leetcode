# Last updated: 6/4/2025, 9:19:18 PM
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        # Step 1: Count the occurrences of each string
        count = {}
        for s in arr:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        
        # Step 2: Collect distinct strings
        distinct_strings = []
        for s in arr:
            if count[s] == 1:
                distinct_strings.append(s)
        
        # Step 3: Return the k-th distinct string or empty string if not enough distinct strings
        if len(distinct_strings) >= k:
            return distinct_strings[k-1]
        else:
            return ""
