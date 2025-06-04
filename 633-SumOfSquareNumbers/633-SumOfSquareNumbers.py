# Last updated: 6/4/2025, 9:21:58 PM
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0: return True;
        if c % 2 == 0: return Solution().judgeSquareSum(c/2);
        if c % 4 != 1: return False;
        
        return sum([c-4*x**2 == int(pow(c-4*x**2, 0.5))**2 for x in range(int(c**0.5/2)+1)]);
        