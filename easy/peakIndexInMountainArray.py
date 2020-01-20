class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        
        start = 0
        end = len(A)
        pivot = (start + end) // 2
        
        while(start < end):
            pivot = (start + end) // 2
            if pivot == 0 and A[pivot] > A[pivot + 1]:
                return 0
            if pivot == len(A) - 1 and A[pivot] > A[pivot - 1]:
                return len(A) - 1
            if A[pivot] > A[pivot - 1]:
                start = pivot
            if A[pivot] > A[pivot + 1]:
                end = pivot
        
        return start