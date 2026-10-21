class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        final = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in final:
                return [final[complement], i]
            final[val] = i
        return []
