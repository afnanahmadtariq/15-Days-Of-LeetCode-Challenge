class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            s = list(s)
            t = list(t)
            s.sort()
            t.sort()
            for i, char in enumerate(s):
                if char != t[i]:
                    return False
            return True
        