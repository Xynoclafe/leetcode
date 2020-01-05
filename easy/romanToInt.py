class Solution:
    def romanToInt(self, s: str) -> int:
        
        dictionary = {"M" : 1000, "D" : 500, "CM" : 900, "CD" : 400, "C" : 100, "L" : 50, "X" : 10, "XC" : 90, "XL" : 40, "V" : 5, "I" : 1, "IX" : 9, "IV" : 4}
        
        i = 0
        num = 0
        
        while i in range(len(s)):
            char = s[i]
            if char not in {"I", "X", "C"}:
                num += dictionary[char]
                i += 1
            else:
                if i + 1 < len(s):
                    completeChar = char + s[i + 1]
                    if completeChar in dictionary:
                        num += dictionary[completeChar]
                        i += 2
                    else:
                        num += dictionary[char]
                        i += 1
                else:
                    num += dictionary[char]
                    i += 1
        return num