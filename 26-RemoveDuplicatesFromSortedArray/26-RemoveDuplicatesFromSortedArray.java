// Last updated: 6/4/2025, 9:23:57 PM
class Solution {
    public int removeDuplicates(int[] nums) {
        int pointer1 = 1;
        for (int pointer2 = 1; pointer2<nums.length; pointer2++) {
            if (nums[pointer2] != nums[pointer2 - 1]) {
                nums[pointer1] = nums[pointer2];
                pointer1++;
            }
        }
        return pointer1;
    }
}