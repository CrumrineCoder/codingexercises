from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        fbL = []

        for i in range(1, n + 1):
            to_add = None
            if (i % 3 == 0 and i % 5 == 0):
                to_add = "FizzBuzz"
            elif (i % 3 == 0):
                to_add = "Fizz"
            elif (i % 5 == 0):
                to_add = "Buzz"
            else:
                to_add = i
            fbL.append(str(to_add))

        return fbL

sol = Solution()
print(sol.fizzBuzz(3))