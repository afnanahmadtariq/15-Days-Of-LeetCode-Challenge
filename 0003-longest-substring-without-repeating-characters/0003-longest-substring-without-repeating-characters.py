class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strings = []
        long = ""
        for sub in s:
            if sub in long:
                strings = strings + [long]
                long = long[long.index(sub)+1:] +sub
            else:
                long += sub
        strings = strings + [long]
        return max([len(s) for s in strings])