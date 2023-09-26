dp = [-1 for _ in range(46)]
dp[0] = 1
dp[1] = 1


def aux(n):
    if dp[n] == -1:
        dp[n] = aux(n - 1) + aux(n - 2)
    return dp[n]


class Solution:
    def climbStairs(self, n: int) -> int:
        return aux(n)


sol = Solution()
ans = sol.climbStairs(11)
print("ans", ans)
