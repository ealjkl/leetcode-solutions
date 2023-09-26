from typing import List
import math


def maximum_subarray_and_indexes(nums):
    n = len(nums)
    if n == 0:
        return [-math.inf, 0, 0]
    a = 0
    b = 1
    maxCandidate = [nums[0], a, b]
    current = [nums[0], a, b]
    for i in range(1, n):
        candidate1 = [nums[i], i, i + 1]
        candidate2 = [current[0] + nums[i], current[1], current[2] + 1]
        current = max([candidate1, candidate2])
        maxCandidate = max([current, maxCandidate])
    return maxCandidate


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        first = nums[:n//2]
        second = nums[n//2:][::-1]
        first_max = maximum_subarray_and_indexes(first)
        second_max = maximum_subarray_and_indexes(second)
        second_max[2], second_max[1] = n - second_max[1], n - second_max[2]
        bridge1 = [first_max[2], second_max[1]]
        bridge21 = [0, first_max[1]]
        bridge22 = [second_max[2], n]
        candidate_1 = first_max[0]
        candidate_2 = second_max[0]
        candidate_3 = first_max[0] + \
            sum(nums[bridge1[0]: bridge1[1]]) + second_max[0]
        candidate_4 = first_max[0] + sum(nums[bridge21[0]: bridge21[1]]) + sum(
            nums[bridge22[0]: bridge22[1]]) + second_max[0]
        ans = max([candidate_1, candidate_2, candidate_3, candidate_4])
        return ans


sol = Solution()
x = sol.maxSubarraySumCircular([-2])
print(x)
