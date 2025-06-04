// Last updated: 6/4/2025, 9:20:22 PM
public class Solution {
    public int numSteps(String s) {
        int steps = 0;
        int carry = 0;
        
        // Start from the end of the string (least significant bit)
        for (int i = s.length() - 1; i > 0; i--) {
            int digit = s.charAt(i) - '0';
            
            // If current digit + carry is odd
            if (digit + carry == 1) {
                steps += 2; // Need 2 steps: add 1 and then divide by 2
                carry = 1; // Update carry for next iteration
            } else {
                steps += 1; // Need 1 step: divide by 2
            }
        }
        
        // If there's still a carry left, add one more step
        steps += carry;
        
        return steps;
    }
}
