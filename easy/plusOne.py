class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while True:
            if i < 0:
                return [1] + digits
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
                i -= 1
