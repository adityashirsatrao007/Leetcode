// Last updated: 6/4/2025, 9:18:39 PM
class Solution {
    public int[] applyOperations(int[] nums) {
        int n = nums.length;

        // Apply operations
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] == nums[i + 1]) {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }

        // Shift non-zero elements in-place
        int index = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] != 0) {
                nums[index++] = nums[i];
            }
        }

        // Fill remaining positions with zero
        while (index < n) {
            nums[index++] = 0;
        }

        return nums;
    }
}
