// Last updated: 6/4/2025, 9:18:37 PM
class Solution {
    public int distinctAverages(int[] nums) {
        //sort the array
        Arrays.sort(nums);
        //assign pointers
        int min=0;
        int max=nums.length-1;
//storing unique averages in it
        HashSet<Double> hs=new HashSet<>();

        while(min<max){
            double avg=(nums[min]+nums[max])/2.0;
            hs.add(avg);
            min++;
            max--;
        }
return hs.size();

    }
}