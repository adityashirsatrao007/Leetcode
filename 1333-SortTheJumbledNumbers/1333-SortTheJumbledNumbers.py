# Last updated: 6/4/2025, 9:20:50 PM
class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        def get_mapped_value(num):
            mapped_num = ""
            for digit in str(num):
                mapped_num += str(mapping[int(digit)])
            return int(mapped_num)
        
        mapped_nums = [(get_mapped_value(num), num) for num in nums]
        mapped_nums.sort(key=lambda x: x[0])
        sorted_nums = [num for _, num in mapped_nums]
        
        return sorted_nums
