class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        
        s = str(x)
        rev = s[::-1]

        if s == rev:
            return True
        return False