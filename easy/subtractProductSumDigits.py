class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nSum = 0
        nProduct = 1
        while n:
            digit = n % 10
            nSum += digit
            nProduct *= digit
            n = n // 10
        return nProduct - nSum
        