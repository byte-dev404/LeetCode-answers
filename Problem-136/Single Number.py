class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result

test = Solution()
print(test.singleNumber([4,2,4,1,2]))