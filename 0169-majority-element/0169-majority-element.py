class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = collections.Counter()
        count.update(nums)
        num = max(count.values())
        for key, value in count.items():
            if value == num:
                return key

        