from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        L = 1
        R = n
        while L <= R:
            M = L + (R - L)//2
            greater = M + 1
            if 0 <= M + 1 < len(nums) and nums[M + 1] == nums[M]:
                return -1
            elif 0 <= M - 1 < len(nums) and nums[M - 1] == nums[M - 1]:
                return -1
            return greater
