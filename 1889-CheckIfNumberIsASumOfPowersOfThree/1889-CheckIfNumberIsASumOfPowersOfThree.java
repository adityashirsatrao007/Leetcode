// Last updated: 6/4/2025, 9:19:39 PM
class Solution {
    public boolean checkPowersOfThree(int n) {
       String base3 = Integer.toString(n, 3);
        
        return !base3.contains("2");  
    }
}