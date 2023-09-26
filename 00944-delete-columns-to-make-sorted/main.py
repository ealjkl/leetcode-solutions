from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        total_to_remove = 0
        for c in range(len(strs[0])):
            for r in range(1, len(strs)):
                if (strs[r][c] < strs[r - 1][c]):
                    total_to_remove += 1
                    break
        return total_to_remove


sol = Solution()
inp = ["cba", "daf", "ghi"]
sol.minDeletionSize(inp)
