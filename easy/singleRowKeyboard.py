from collections import defaultdict
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        index = 0
        pos = defaultdict(lambda: -1)
        keyStrokes = 0
        j = 0
        i = 0
        for j in range(len(word)):
            if pos[word[j]] != -1:
                keyStrokes += abs(pos[word[j]] - index)
                index = pos[word[j]]
            else:
                while i < 26:
                    pos[keyboard[i]] = i
                    if word[j] == keyboard[i]:
                        keyStrokes += abs(pos[word[j]] - index)
                        index = pos[word[j]]
                    i += 1
        return keyStrokes