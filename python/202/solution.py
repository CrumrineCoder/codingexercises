class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            digits = list(str(n))
            n = sum(int(digit) ** 2 for digit in digits)

        return n == 1