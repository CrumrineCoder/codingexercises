class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = bin(x)[2:]
        y = bin(y)[2:]

        differences = 0

        max_len = max(len(x), len(y))
        x = x.zfill(max_len)
        y = y.zfill(max_len)

        for i in range(0, len(x)):
            if (x[i] != y[i]):
                differences += 1
        return differences