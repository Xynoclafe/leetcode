from collections import defaultdict
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        position = defaultdict(lambda: (10 ** 10))
        
        for i in range(len(arr2)):
            position[arr2[i]] = i
            
        arr1.sort()
            
        return sorted(arr1, key = lambda i: position[i])