class Solution:
   def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        lSum = 0  
        for i, num in enumerate(nums):
            rSum = total_sum - lSum - num 
            if lSum == rSum:
                return i
            lSum += num
        return -1
