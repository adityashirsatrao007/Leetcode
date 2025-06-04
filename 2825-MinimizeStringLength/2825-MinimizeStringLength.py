# Last updated: 6/4/2025, 9:18:07 PM
class Solution:
    def minimizedStringLength(self, s: str) -> int:
        a=""
        for i in s:
            if(i not in a):
                a+=i
        return(len(a))