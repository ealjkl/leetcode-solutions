from collections import Counter
from typing import List


def find_minimum_per_level(count):
    if (count == 1):
        return -1
    if (count % 3 == 0):
        return count // 3
    if (count % 3 == 1):
        return (count - 3) // 3 + 2
    if (count % 3 == 2):
        return (count - 2) // 3 + 1


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        total = 0
        for count in counter.values():
            min_this_level = find_minimum_per_level(count)
            if min_this_level == -1:
                return -1
            else:
                total += min_this_level
        return total


sol = Solution()
ans = sol.minimumRounds([2, 3, 3])
print("ans", ans)
