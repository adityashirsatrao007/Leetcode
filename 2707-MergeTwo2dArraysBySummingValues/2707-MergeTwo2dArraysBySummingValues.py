# Last updated: 6/4/2025, 9:18:20 PM
class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        from collections import defaultdict

        merged_dict = defaultdict(int)
        
        for id_val in nums1:
            merged_dict[id_val[0]] += id_val[1]

        for id_val in nums2:
            merged_dict[id_val[0]] += id_val[1]

        result = [[key, merged_dict[key]] for key in sorted(merged_dict.keys())]
        
        return result
