class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for num in nums:
            if nums[index] == 0:
                nums.pop(index)
                nums.append(0)
            else:
                index += 1