class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 0
        while True:
            if 2 ** power == n:
                return True
            elif 2 ** power < n:
                power+=1
            else:
                return False