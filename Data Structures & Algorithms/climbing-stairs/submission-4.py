class Solution:
    def climbStairs(self, n: int) -> int:
    #     sqrt5 = math.sqrt(5)
    #     phi = (1 + sqrt5) / 2
    #     psi = (1 - sqrt5) / 2
    #     n += 1
    #     return round((phi**n - psi**n) / sqrt5)


    # def climbStairs(n):
        a, b = 1, 1

        for _ in range(n):
            a, b = b, a + b

        return a