class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        validAns = []
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            if(nums[0] >= s):
                return [nums[0],nums[0]]
            else:
                return 0
        if(len(nums) == 2):
            if(nums[0] + nums[1] >= s):
                return [nums[0],nums[1]]
            else:
                return 0
        else:
            fp = 0
            sp = 0
            sum = nums[fp]
            while(sp <= len(nums)):
                #print(fp, sp, sum)
                if sum < s:
                    sp += 1
                    if(sp < len(nums)):
                        sum += nums[sp]
                elif sum >= s:
                    validAns.append([fp, sp, sum])
                    sum -= nums[fp]
                    if(fp == sp):
                        sp += 1
                        if(sp < len(nums)):
                            sum += nums[sp]
                    fp += 1
        minLen = 10**10
        for item in validAns:
            minLen = min(minLen, item[1] - item[0])
        if(len(validAns) == 0):
            return 0
        else:
            return minLen + 1
