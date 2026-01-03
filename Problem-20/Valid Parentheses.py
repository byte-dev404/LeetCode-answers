class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')': '(', '}': '{', ']': '['}

        for i in s:
            if i in '({[': stack.append(i)
            else:
                if not stack: return False
                elif stack.pop() != pairs[i]: return False
        return not stack