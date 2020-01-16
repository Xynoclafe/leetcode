class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        subS = []
        if length == 1:
            return False
        for i in range(length):
            if len(subS) == 0:
                if s[i] * length == s:
                    return True
                else:
                    subS.append(s[i])
            else:
                if s[i] != subS[0]:
                    subS.append(s[i])
                else:
                    if i != length -1 and length % len(subS) == 0:
                        if "".join(subS * (length // len(subS))) == s:
                            return True
                        else:
                            subS.append(s[i])
                    else:
                        subS.append(s[i])
        return False