from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            dictionary[key].append(word)
        returnList = []
        for key in dictionary:
            returnList.append(dictionary[key])
        return returnList
