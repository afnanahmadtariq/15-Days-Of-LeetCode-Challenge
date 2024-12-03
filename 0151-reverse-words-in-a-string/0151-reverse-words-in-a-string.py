class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        s = s.split()
        s.reverse()
        s = ' '.join(s)
        return s
        