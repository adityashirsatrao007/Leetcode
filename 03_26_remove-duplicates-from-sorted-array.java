class Solution {
    public int removeDuplicates(int[] nums) {
        int j = 1; // Step 1: Initialize j to 1
        for (int i = 1; i < nums.length; i++) { // Step 2: Loop i from 1 to end
            if (nums[i] != nums[i - 1]) { // Step 3: Check if current != previous
                nums[j] = nums[i]; // Step 4: Copy unique element at index i to index j
                j++; // Step 5: Increment j for next unique spot
            }
        }
        return j; // Step 6: Return count of unique elements
    }
}



