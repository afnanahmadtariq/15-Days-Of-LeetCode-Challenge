class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        lSum = 0
        rSum = sum(n for n in nums) - nums[0]
        length = len(nums)
        for i, num in enumerate(nums):
            if lSum == rSum:
                return i
            lSum += num
            if i < length-1:
                rSum -= nums[i + 1]
        return -1