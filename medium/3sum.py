class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums) < 3):
            return []
        nums.sort()
        negs = []
        combos = []
        while(len(nums) > 0 and nums[0] < 0):
            negs.append(nums.pop(0))
        if(len(nums) == 0):
            return []
        ocount = 0
        for i in range(len(nums)):
                if(nums[i] == 0):
                    ocount += 1
                else:
                    break
        if(ocount >= 3):
            combos.append([0,0,0])
        for neg in negs:
            fp = 0
            sp = len(nums) - 1
            while(sp > 0 and fp < len(nums)):
                if(sp == fp):
                    break
                sum = neg + nums[fp] + nums[sp]
                if(sum == 0):
                    combos.append(sorted([neg, nums[fp], nums[sp]]))
                    fp += 1
                    sp -= 1
                elif(sum < 0):
                    fp += 1
                elif(sum > 0):
                    sp -= 1
        for num in nums:
            fp = 0
            sp = len(negs) - 1
            while(sp > 0 and fp < len(negs)):
                if(sp == fp):
                    break
                sum = num + negs[fp] + negs[sp]
                if(sum == 0):
                    combos.append(sorted([num, negs[fp], negs[sp]]))
                    fp += 1
                    sp -= 1
                elif(sum < 0):
                    fp += 1
                elif(sum > 0):
                    sp -= 1
        combos.sort()
        i = 0
        while i in range(len(combos) - 1):
            if(set(sorted(combos[i])) == set(sorted(combos[i+1]))):
                combos.pop(i+1)
            else:
                i += 1
        return combos
