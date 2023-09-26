from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ans = 0
        for cost in costs:
            coins -= cost
            if (coins < 0):
                break
            ans += 1
        return ans


sol = Solution()
ans = sol.maxIceCream([1, 3, 2, 4, 1], 7)
print("ans", ans)
