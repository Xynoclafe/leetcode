class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        
        minSwaps = dict()
        
        def swapIndex(A, B, i):
            A[i], B[i] = B[i], A[i]
            return A, B
        
        def swaps(A, B, i, swap):
            if i == len(A):
                return 0
            
            if (swap, i) in minSwaps:
                return minSwaps[(swap,i)]
            
            min1 = float("inf")
            if A[i] > A[i - 1] and B[i] > B[i-1]:
                min1 = swaps(A, B, i + 1, 0)
            
            min2 = float("inf")
            if B[i] > A[i - 1] and A[i] > B[i - 1]:
                A, B = swapIndex(A, B, i)
                min2 = 1 + swaps(A, B, i + 1, 1)
                A, B = swapIndex(A, B, i)
            
            minSwaps[(swap, i)] = min(min1, min2)
            return minSwaps[(swap, i)]
        
        if len(A) == 0:
            return 0
        else:
            return min(swaps(A, B, 1, 0), 1 + swaps([B[0]] + A[1:], [A[0]] + B[1:], 1, 1))
