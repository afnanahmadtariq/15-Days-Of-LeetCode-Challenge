class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter()
        count.update(list(s))
        for char, occurance in count.items():
            if occurance == 1:
                return s.index(char)
        return -1