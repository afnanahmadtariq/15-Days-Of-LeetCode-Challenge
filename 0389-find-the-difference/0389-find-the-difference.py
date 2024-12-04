class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        t.sort()
        s = list(s)
        s.sort()
        print(t)
        print(s)
        for i, c in enumerate(t):
            if i > len(s)-1:
                return c
            elif c != s[i]:
                return c