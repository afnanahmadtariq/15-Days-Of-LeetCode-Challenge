class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ''
        current = chars[0]
        count = 0
        for c in chars:
            if c == current:
                count += 1
            else:
                s += current + (str(count) if count > 1 else '')
                current = c
                count = 1
        s += current + (str(count) if count > 1 else '')
        chars[:] =  list(s)
        return len(chars)