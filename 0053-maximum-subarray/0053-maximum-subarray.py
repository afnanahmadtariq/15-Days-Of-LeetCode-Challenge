class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = nums[0]
        for i in range(1,len(nums)):
            currentSum = max(currentSum + nums[i], nums[i])
            maxSum = max(maxSum, currentSum)
        return maxSum