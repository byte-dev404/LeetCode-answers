class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman_hashTable = {
            'IV': 4,
            'IX': 9,
            'I': 1,
            'V': 5,
            'XL': 40,
            'XC': 90,
            'X': 10,
            'L': 50,
            'CD': 400,
            'CM': 900,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        symbols = list(s.upper())
        num = 0
        i = 0
        
        while i < len(symbols):
            if i + 1 < len(symbols):
                two = symbols[i] + symbols[i + 1]
                if two in roman_hashTable:
                    num += roman_hashTable[two]
                    i += 2
                    continue
            num += roman_hashTable[symbols[i]]
            i += 1
            
        return num