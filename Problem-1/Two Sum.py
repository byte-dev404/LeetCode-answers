class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        results = {}
        for index, num in enumerate(nums):
            left = target - num
            if left in results:
                return [results[left], index]
            results[num] = index

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

test = Solution()
print(test.twoSum([2,7,11,15], 9))
