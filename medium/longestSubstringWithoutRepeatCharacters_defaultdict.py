from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dictionary = defaultdict(lambda: -1)
        count = 0
        maxCount = 0
        lastLocation = 0
        for i in range(len(s)):
            if dictionary[s[i]] == -1:
                dictionary[s[i]] = i
                count += 1
            else:
                if lastLocation > dictionary[s[i]]:
                    dictionary[s[i]] = i
                    count += 1 
                else:
                    if maxCount < count:
                        maxCount = count
                    count = i - dictionary[s[i]]
                    lastLocation = dictionary[s[i]]
                    dictionary[s[i]] = i
        
        return max(maxCount, count)
