class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        swapA1 = 0
        swapB1 = 0
        swapA2 = 1
        swapB2 = 1
        A1stat = True
        A2stat = True
        B1stat = True
        B2stat = True
        for i in range(1, len(A)):
            if(A1stat):
                if(A[i] != A[0] and A[0] == B[i]):
                    swapA1 += 1
                elif(A[i] != A[0]):
                    #print(i, AA[i])
                    swapA1 = 10 ** 10
                    A1stat = False
            if(A2stat):
                if(A[i] != B[0] and B[0] == B[i]):
                    swapA2 += 1
                elif(A[i] != B[0]):
                    #print(i, AA[i])
                    swapA2 = 10 ** 10
                    A2stat = False
            if(B1stat):
                if(B[i] != B[0] and B[0] == A[i]):
                    swapB1 += 1
                elif(B[i] != B[0]):
                    #print(i, B[i])
                    swapB1 = 10 ** 10
                    B1stat = False
            if(B2stat):
                if(B[i] != A[0] and A[0] == A[i]):
                    swapB2 += 1
                elif(B[i] != A[0]):
                    #print(i, B[i])
                    swapB2 = 10 ** 10
                    B2stat = False
        #print(swapA1, swapA2, swapB1, swapB2)
        swapMin = min(swapA1, swapA2, swapB1, swapB2)
        if(swapMin != 10 ** 10):
            return swapMin
        else:
            return -1
