from typing import List


def is_in_range(x, ran):
    x0, x1 = ran
    return x0 <= x <= x1


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 1
        points.sort()
        print(points)
        current_range = points[0]
        for (x0, x1) in points[1:]:
            if is_in_range(x0, current_range):
                current_range = [max(current_range[0], x0),
                                 min(current_range[1], x1)]
            else:
                current_range = [x0, x1]
                ans += 1
            # print("current range", current_range)
        return ans


sol = Solution()
ans = sol.findMinArrowShots(
    [[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]])
print("ans", ans)
