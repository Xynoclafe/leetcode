from collections import defaultdict
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def buildSequences(key, keys):
            seen[tuple(sorted(key))] = True
            for i in range(len(keys)):
                if not seen[tuple(sorted(key + [keys[i]]))]:
                    if i < len(keys) - 1:
                        buildSequences(key + [keys[i]], keys[:i] + keys[i + 1:])
                    else:
                        buildSequences(key + [keys[i]], keys[:i])
            return
        
        keys = nums
        seen = defaultdict(lambda: False)
        
        
        for i in range(len(keys)):
            if not seen[tuple([keys[i]])]:
                if i < len(keys) - 1:
                    buildSequences([keys[i]], keys[:i] + keys[i + 1:])
                else:
                    buildSequences([keys[i]], keys[:i])
        
        returnList = [[]]
        for key in seen:
            returnList.append((list(key)))
        return returnList