# Last updated: 6/4/2025, 9:22:29 PM
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"

        below_20 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
                    'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        tens = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']

        def helper(n):
            if n < 20:
                return below_20[n]
            elif n < 100:
                return tens[n // 10] + ('' if n % 10 == 0 else ' ' + below_20[n % 10])
            else:
                return below_20[n // 100] + ' Hundred' + ('' if n % 100 == 0 else ' ' + helper(n % 100))

        res = ''
        for i, unit in enumerate(thousands):
            if num % 1000 != 0:
                res = helper(num % 1000) + ' ' + unit + ('' if res == '' else ' ' + res)
            num //= 1000
        
        return res.strip()

# Example usage:
# sol = Solution()
# print(sol.numberToWords(123)) # "One Hundred Twenty Three"
# print(sol.numberToWords(12345)) # "Twelve Thousand Three Hundred Forty Five"
# print(sol.numberToWords(1234567)) # "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
