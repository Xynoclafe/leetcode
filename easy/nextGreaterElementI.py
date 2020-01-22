from collections import deque
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreatest = defaultdict(lambda : -1)
        
        stack = deque()
        
        for num in nums2:
            if len(stack) == 0 or num <= stack[-1]:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    nextGreatest[stack.pop()] = num
                stack.append(num)
        
        answer = deque()
        
        for num in nums1:
            answer.append(nextGreatest[num])
        
        return answer
