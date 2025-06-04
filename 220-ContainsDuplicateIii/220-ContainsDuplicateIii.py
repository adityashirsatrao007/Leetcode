# Last updated: 6/4/2025, 9:22:39 PM
class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        buckets = {}
        bucket_size = valueDiff + 1
        
        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            if bucket_id in buckets:
                return True
            if bucket_id - 1 in buckets and abs(buckets[bucket_id - 1] - num) <= valueDiff:
                return True
            if bucket_id + 1 in buckets and abs(buckets[bucket_id + 1] - num) <= valueDiff:
                return True
            
            buckets[bucket_id] = num
            if i >= indexDiff:
                del buckets[nums[i - indexDiff] // bucket_size]
        
        return False
