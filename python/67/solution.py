class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num_a = int(a, 2)
        num_b = int(b, 2) 

        sum_decimal = num_a + num_b

        return bin(sum_decimal)[2:]