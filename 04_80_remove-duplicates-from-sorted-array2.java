class Solution {
    public int removeDuplicates(int[] nums) {
        if (nums.length <= 2) {
            return nums.length;
        }

        int pointer1 = 2;

        for (int pointer2 = 2; pointer2 < nums.length; pointer2++) {
            if (nums[pointer2] != nums[pointer1 - 2]) {
                nums[pointer1] = nums[pointer2]; // ✅ fix is here
                pointer1++;
            }
        }
        return pointer1;
    }
}
