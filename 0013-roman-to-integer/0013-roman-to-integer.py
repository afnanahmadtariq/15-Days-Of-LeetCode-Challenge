class Solution:
    def romanToInt(self, s: str) -> int:
        nums = {
            'I':1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        num = nums[s[0]]
        for i, char in enumerate(s):
            if i+1 < len(s):
                if nums[char] >= nums[s[i+1]]:
                    num += nums[s[i+1]]
                else:
                    num += nums[s[i+1]] - (nums[char]*2)
        return num
                
