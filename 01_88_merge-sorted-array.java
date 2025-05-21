class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        for (int j=0, i=m, j<n, j++) {
            nums1[i] = nums2[j];
            i++;
        }
        Arrays.sort(nums1);
    }
}

//j=0 : first element in nums2
//i=m : adding the elements of nums2 in nums1 at i=mth position i.e. after the filled postion of nums1 elements
//j<n : iteration untill all elements in nums2 
//i++ : iteration over empty spaces in nums1
//nums1[i] = nums2[j] : denote elements of nums2 in nums1 