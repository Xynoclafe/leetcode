from collections import defaultdict
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        deadends = set(deadends)
        seen = defaultdict(lambda: False)
        
        l1 = ["0000"]
        l2 = []
        
        
        def check(combo):
            if not seen[combo] and combo not in deadends:
                seen[combo] = True
                l2.append(combo)
                if combo == target:
                    return count + 1
                else:
                    return -1
            else:
                return -1
        
        if "0000" in deadends and target != "0000":
            return -1
        
        count = 0
        while len(l1) > 0:
            curCombo = l1.pop(0)
            if curCombo == target:
                return count
            for i in range(4):
                if i > 0 and i < 3:
                    nCombo1 = curCombo[:i] + str((int(curCombo[i]) + 1) % 10) + curCombo[i+1:]
                    nCombo2 = curCombo[:i] + str((int(curCombo[i]) - 1) % 10) + curCombo[i+1:]
                    
                elif i == 0:
                    nCombo1 = str((int(curCombo[i]) + 1) % 10) + curCombo[i+1:]
                    nCombo2 = str((int(curCombo[i]) - 1) % 10) + curCombo[i+1:]
                else:
                    nCombo1 = curCombo[:i] + str((int(curCombo[i]) + 1) % 10)
                    nCombo2 = curCombo[:i] + str((int(curCombo[i]) - 1) % 10)
                    
                check1 = check(nCombo1)
                check2 = check(nCombo2)
                    
                if check1 != -1 or check2 != -1:
                    return max(check1, check2)
                    
            if len(l1) == 0:
                count += 1
                l1 = l2
                l2 = []
        return -1
            