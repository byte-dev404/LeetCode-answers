class Solution:
    def isPalindrome(self, s: str) -> bool:
        non_numerical_str = ''
        
        for i in s.lower():
            if i in 'abcdefghijklmnopqrstuvwxyz0123456789':
                non_numerical_str += i
        
        if non_numerical_str != non_numerical_str[::-1]:
            return False
        return True
    
    

test = Solution()
print(test.isPalindrome(''))