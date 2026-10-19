class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        itr= set()
        for i in nums:
            if i in itr:
                return True
            itr.add(i)
        return False
