class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for string in strs:
            if not string.startswith(prefix):
                for i in range(0, len(prefix)+1):
                    if string.startswith(prefix[:len(prefix)-i]):
                        prefix = prefix[:len(prefix)-i]
                        break
        return prefix