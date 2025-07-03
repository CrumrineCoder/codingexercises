
class Solution:
   def mySqrt(self, x: int) -> int:
       low = 0
       high = x
       while low <= high:
           bestGuess = (low + high) // 2
           if bestGuess * bestGuess == x:
               return bestGuess
           elif bestGuess * bestGuess < x:
               low = bestGuess + 1
           else:
               high = bestGuess - 1
       return high

sol = Solution()
print(sol.mySqrt(8))