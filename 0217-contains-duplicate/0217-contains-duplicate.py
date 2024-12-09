class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = collections.Counter()
        for num in nums:
            count[num] += 1
            if count[num] > 1:
                return True
        return False