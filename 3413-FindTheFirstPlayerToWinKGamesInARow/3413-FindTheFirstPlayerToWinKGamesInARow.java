// Last updated: 6/4/2025, 9:17:50 PM
public class Solution {
    public int findWinningPlayer(int[] skills, int k) {
        int n = skills.length;
        int currentWinner = 0; // Start with the first player
        int winCount = 0;

        for (int i = 1; i < n; i++) {
            if (skills[currentWinner] > skills[i]) {
                winCount++;
            } else {
                currentWinner = i;
                winCount = 1;
            }
            
            if (winCount == k) {
                return currentWinner;
            }
        }
        
        return currentWinner; // If no player wins k times consecutively, the player with the most wins is returned
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] skills1 = {4, 2, 6, 3, 9};
        int k1 = 2;
        System.out.println(solution.findWinningPlayer(skills1, k1)); // Expected Output: 2
        
        int[] skills2 = {2, 5, 4};
        int k2 = 3;
        System.out.println(solution.findWinningPlayer(skills2, k2)); // Expected Output: 1
    }
}
