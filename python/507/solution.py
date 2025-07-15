class Solution:
    def checkPerfectNumber(self, num: int) -> bool:

        if (num <= 1):
            return False
        divisors = {1}

        for n in range(2, int(num ** 0.5) + 1):
            if (num % n == 0):
                divisors.add(n)
                if n != num // n:
                    divisors.add(num // n)
        return sum(divisors) == num