from collections import defaultdict
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def buildSequences(key, keys):
            seen[key] = True
            for i in range(len(keys)):
                if not seen[key + keys[i]]:
                    if i < len(keys) - 1:
                        buildSequences(key + keys[i], keys[:i] + keys[i + 1:])
                    else:
                        buildSequences(key + keys[i], keys[:i])
            return
        
        keys = [i for i in tiles]
        seen = defaultdict(lambda: False)
        
        for i in range(len(keys)):
            if not seen[keys[i]]:
                if i < len(keys) - 1:
                    buildSequences(keys[i], keys[:i] + keys[i + 1:])
                else:
                    buildSequences(keys[i], keys[:i])
        
        return(len(seen))