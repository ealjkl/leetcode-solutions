from typing import List
import math


def max_sub_array_and_start(array):
    min_sum = [array[0], -1]
    max_sum = [array[0], -1]
    curr_min = [math.inf, -1]
    curr_max = [-math.inf, -1]
    total = 0
    for i, num in enumerate(array):
        curr_min = min([curr_min[0] + num, i + 1], [num, i + 1])
        min_sum = min(min_sum, curr_min)

        curr_max = max([curr_max[0] + num, curr_max[1]], [num, i])
        max_sum = max(max_sum, curr_max)
        total += num
    # print("max_sum", max_sum)
    # print("min_sum", min_sum)
    return max(max_sum, [total - min_sum[0], (min_sum[1]) % len(array)]) if max_sum > [0, -1] else max_sum


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        array = [gas[i] - cost[i] for i in range(len(gas))]
        # print("array", array)
        max_sub = max_sub_array_and_start(array)
        _, index = max_sub
        tot = 0
        # print("index", index)
        for num in array[index:]:
            tot += num
            if (tot < 0):
                return -1
        for num in array[:index]:
            tot += num
            if tot < 0:
                return -1
        return index


sol = Solution()
ans = sol.canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6])

print(ans)
