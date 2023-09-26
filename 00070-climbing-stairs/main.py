def factorial(b):
    if b == 0:
        return 1
    return factorial(b - 1)*b


def non_repeating(a, b):
    if (b > a):
        a, b = b, a
    prod = 1
    for i in range(a + 1, a + b + 1):
        prod *= i
    return prod/factorial(b)


class Solution:
    def climbStairs(self, n: int) -> int:
        total = 0
        for i in range(n//2 + 1):
            a, b = i, n - 2*i
            non_rep = non_repeating(a, b)
            total += non_rep
        return int(total)


sol = Solution()
ans = sol.climbStairs(11)
print("ans", ans)
