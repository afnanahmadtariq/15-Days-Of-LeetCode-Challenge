class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        s = list(s)
        count = collections.Counter()
        count.update(t)
        count = count - Counter(s)
        for c, i in count.items():
            if i > 0:
                return c