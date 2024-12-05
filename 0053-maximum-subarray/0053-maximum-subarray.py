class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]
        for i, num in enumerate(nums):
            if i == 0:
                continue
            currentSum = max(currentSum + num, num)
            maxSum = max(maxSum, currentSum)
        return maxSum