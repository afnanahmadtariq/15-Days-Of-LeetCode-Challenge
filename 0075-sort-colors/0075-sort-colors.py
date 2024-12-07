class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        for _ in nums:
            if nums[i] == 0:
                nums.pop(i)
                nums[:] = [0] + nums
                i += 1
            elif nums[i] == 2:
                nums.remove(2)
                nums.append(2)
            else:
                i += 1

        