class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionary = dict()
        maxNum = 0
        count = 0
        lastLocation = 0
        for i in range(len(s)):
            if not s[i] in dictionary.keys():
                dictionary[s[i]] = i
                count += 1
            else:
                if lastLocation > dictionary[s[i]]:
                    dictionary[s[i]] = i
                    count += 1 
                else:
                    if maxNum < count:
                        maxNum = count
                    count = i - dictionary[s[i]]
                    lastLocation = dictionary[s[i]]
                    dictionary[s[i]] = i
        if maxNum < count:
            maxNum = count
        return maxNum
