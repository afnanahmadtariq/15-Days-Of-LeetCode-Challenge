class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        max_value = nums[0]
        left_value = right_value = 1
        
        for i in range(n):
            # Left to right pass
            left_value *= nums[i]
            max_value = max(max_value, left_value)
            if left_value == 0:
                left_value = 1  # Reset if zero is encountered
            
            # Right to left pass
            right_value *= nums[n - i - 1]
            max_value = max(max_value, right_value)
            if right_value == 0:
                right_value = 1  # Reset if zero is encountered

        return max_value