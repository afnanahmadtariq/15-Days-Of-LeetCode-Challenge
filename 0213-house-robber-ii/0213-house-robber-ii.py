class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        fRob2, fRob1 = 0, 0
        for i in range(0, len(nums)-1):
            temp = max(nums[i] + fRob2, fRob1)
            fRob2 = fRob1
            fRob1 = temp
        sRob2, sRob1 = 0, 0
        for i in range(1, len(nums)):
            temp = max(nums[i] + sRob2, sRob1)
            sRob2 = sRob1
            sRob1 = temp
        return max(fRob1, sRob1)
            