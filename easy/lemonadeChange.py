from collections import defaultdict
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        billsInHand = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                billsInHand[5] += 1
            elif bill == 10:
                if billsInHand[5] > 0:
                    billsInHand[10] += 1
                    billsInHand[5] -= 1
                else:
                    return False
            elif bill == 20:
                if billsInHand[5] > 0 and billsInHand[10] > 0:
                    billsInHand[5] -= 1
                    billsInHand[10] -= 1
                elif billsInHand[5] > 2:
                    billsInHand[5] -= 3
                else:
                    return False
                billsInHand[20] += 1
        
        return True
