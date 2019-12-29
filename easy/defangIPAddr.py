class Solution:
    def defangIPaddr(self, address: str) -> str:
        retString = ""
        replace = "[.]"
        for i in address:
            if i != ".":
                retString += i
            else:
                retString += replace
        return retString
