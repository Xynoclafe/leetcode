class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = [c for c in s]
        list2 = [c for c in t]
        
        if sorted(list1) == sorted(list2):
            return True
        else:
            return False