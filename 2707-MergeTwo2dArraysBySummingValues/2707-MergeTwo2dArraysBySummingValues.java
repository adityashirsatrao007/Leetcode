// Last updated: 6/4/2025, 9:18:12 PM
class Solution {
    public int[][] mergeArrays(int[][] nums1, int[][] nums2) {
        int m = nums1.length, n = nums2.length;
        int[][] result = new int[m + n][2];
        int p1 = 0, p2 = 0, index = 0;

        while (p1 < m && p2 < n) {
            if (nums1[p1][0] == nums2[p2][0]) {
                result[index++] = new int[]{nums1[p1][0], nums1[p1][1] + nums2[p2][1]};
                p1++;
                p2++;
            } else if (nums1[p1][0] < nums2[p2][0]) {
                result[index++] = nums1[p1++];
            } else {
                result[index++] = nums2[p2++];
            }
        }

        while (p1 < m) result[index++] = nums1[p1++];
        while (p2 < n) result[index++] = nums2[p2++];

        return java.util.Arrays.copyOf(result, index); // Trim extra space
    }
}
