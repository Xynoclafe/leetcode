class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        result = [-1 for _ in range(len(nums))]
        
        for i in range(len(nums)):
            if len(stack) == 0:
                stack.append((nums[i], i))
            elif stack[-1][0] < nums[i]:
                while(stack[-1][0] < nums[i]):
                    num = stack.pop()
                    result[num[1]] = nums[i]
                    if len(stack) == 0:
                        break
                stack.append((nums[i], i))
            else:
                stack.append((nums[i], i))
                
        for i in range(len(nums)):
            if len(stack) == 0:
                break
            while(stack[-1][0] < nums[i]):
                num = stack.pop()
                result[num[1]] = nums[i]
                if len(stack) == 0:
                    break
        
        return result
            