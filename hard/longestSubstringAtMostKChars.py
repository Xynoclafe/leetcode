from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        seen = defaultdict(lambda: -1)
        curStart = 0
        distinct = []
        curLength = 0
        maxLength = 0
        for i in range(len(s)):
            if len(distinct) < k:
                if seen[s[i]] == -1:
                    seen[s[i]] = i
                    distinct.append(i)
                    curLength += 1
                else:
                    distinct.remove(seen[s[i]])
                    distinct.append(i)
                    seen[s[i]] = i
                    curLength += 1
            else:
                if seen[s[i]] >= curStart:
                    distinct.remove(seen[s[i]])
                    distinct.append(i)
                    seen[s[i]] = i
                    curLength += 1
                else:
                    curStart = distinct[0]
                    distinct.pop(0)
                    distinct.append(i)
                    seen[s[i]] = i
                    curLength = i - curStart
                    curStart += 1
            maxLength = max(maxLength, curLength)
        return maxLength