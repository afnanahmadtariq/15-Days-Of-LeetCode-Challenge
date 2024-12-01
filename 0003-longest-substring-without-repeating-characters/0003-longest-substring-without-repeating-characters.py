class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        strings = []
        long = ""
        count = collections.Counter()
        for sub in s:
            print(sub + " and " + long)
            count[sub] += 1
            if count[sub] > 1:
                print(sub + ' :' + str(count[sub]))
                strings = strings + [long]
                for st in long[:long.index(sub)+1]:
                    print(st)
                    count[st] -= 1
                long = long[long.index(sub)+1:] + sub
            else:
                long += sub
        strings = strings + [long]
        print(strings)
        return max([len(s) for s in strings])