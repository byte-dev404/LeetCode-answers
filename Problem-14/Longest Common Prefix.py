class Solution(object):
    def longestCommonPrefix(self, strs):
        i = 0
        while i + 1 < len(strs):
            while strs[0] and strs[0] != strs[i+1][:len(strs[0])]:
                strs[0] = strs[0][:-1]
            i += 1
        return strs[0]