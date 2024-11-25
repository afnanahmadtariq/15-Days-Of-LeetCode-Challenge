class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(not isinstance(s, str)) or 1>len(s)>2*(10**5):
            return False
        else:
            s = s.lower()
            s = ''.join([char for char in s if char.isalnum()])
            if s[:len(s)//2] == s[::-1][:len(s)//2]:
                return True
            else:
                return False