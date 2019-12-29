class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        retlist = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                retlist.append("FizzBuzz")
            elif i % 3 == 0:
                retlist.append("Fizz")
            elif i % 5 == 0:
                retlist.append("Buzz")
            else:
                retlist.append(str(i))
        return retlist
