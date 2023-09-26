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


def get_csum_left(nums):
    n = len(nums)
    out = [nums[0]]
    for i in range(1, n):
        num = nums[i]
        out.append(out[i - 1] + num)
    return out


def get_csum_right(nums):
    return get_csum_left(nums[::-1])[::-1]


def get_cmax_left(nums):
    csum = [0] + get_csum_left(nums)
    out = [csum[0]]
    for i in range(1, len(csum)):
        num = csum[i]
        el = max(out[i - 1], num)
        out.append(el)
    return out


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = maximum_subarray_and_indexes(nums)[0]
        cmax_left = get_cmax_left(nums)
        csum_right = get_csum_right(nums)
        for i in range(n):
            candidate = cmax_left[i] + csum_right[i]
            max_sum = max(max_sum, candidate)
        return max_sum


sol = Solution()
nums = [-2, 2, -2, 9]
x = sol.maxSubarraySumCircular(nums)
print(x)
