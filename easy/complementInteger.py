class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binary = bin(N)
        length = len(binary) - 2
        compString = "1"*length
        compInt = int(compString) - int(binary[2:])
        return(int(str(compInt), 2))
