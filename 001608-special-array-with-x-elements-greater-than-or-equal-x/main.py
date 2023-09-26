from typing import List
from collections import Counter


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        counter = Counter(nums)
        sor = sorted(counter.items(), reverse=True)
        m = len(sor)
        cumsor = [sor[0]]
        for i in range(1, m):
            cumsor.append((sor[i][0], sor[i][1] + cumsor[i - 1][1]))
        ans = -1
        if (cumsor[0][2] == cumsor[0][1]):
            return cumsor[2]

        for i in range(1, m - 1):
            _, cand = cumsor[i]
            if (cumsor[i + 1][0] < cand < cumsor[i - 1][0]):
                ans = cand
                break
        return ans

sol = Solution()
nums = [0, 4, 3, 0, 4]
ans = sol.specialArray(nums)
print("ans", ans)
