# Last updated: 6/4/2025, 9:24:16 PM
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Define the value-symbol pairs for Roman numerals
        value_symbol_pairs = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        roman_numeral = ""
        
        # Convert the number to a Roman numeral
        for value, symbol in value_symbol_pairs:
            while num >= value:
                roman_numeral += symbol
                num -= value
        
        return roman_numeral

# Example usage:
solution = Solution()
print(solution.intToRoman(3749))  # Output: "MMMDCCXLIX"
print(solution.intToRoman(58))    # Output: "LVIII"
print(solution.intToRoman(1994))  # Output: "MCMXCIV"
