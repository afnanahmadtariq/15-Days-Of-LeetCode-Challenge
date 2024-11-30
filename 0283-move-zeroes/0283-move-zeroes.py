class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        while 0 in nums:
            count += 1
            nums.remove(0)
        for i in range(0, count):
            nums.append(0)