class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for count, value in Counter(nums).items():
            if value > 1 :
                return True
        return False