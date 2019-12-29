class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        i = 0
        j = len(A) - 1
        sumList = [-1]
        while(i < j):
            if A[i] + A[j] >= K:
                j -= 1
            elif A[i] + A[j] < K:
                sumList.append(A[i] + A[j])
                i += 1
        sumList.sort()
        return sumList.pop()
            
