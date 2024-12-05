class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index= 0
        length = len(nums)
        for _ in range(0,length):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
        return len(nums)