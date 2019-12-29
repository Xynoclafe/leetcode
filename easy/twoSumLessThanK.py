class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        if min(A) > K:
            return -1
        sumList = [-1]
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                if A[i] + A[j] < K:
                    sumList.append(A[i] + A[j])
        sumList.sort()
        return sumList.pop()
