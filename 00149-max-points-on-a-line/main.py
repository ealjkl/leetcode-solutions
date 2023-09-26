from typing import List


def get_line(point1, point2):
    def is_in_line(point):
        x1, y1 = point1
        x2, y2 = point2
        x, y = point
        return (y1 - y2)*(x1 - x) == (y1 - y)*(x1 - x2)

    return is_in_line


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if (len(points) <= 2): return len(points)
        ma = 2
        for i in range(len(points)):
            point1 = points[i]
            for j in range(i + 1, len(points)):
                point2 = points[j]
                is_in_line = get_line(point1, point2)
                curr = 0
                for point in points:
                    curr += is_in_line(point)
                ma = max(ma, curr)
        return ma


sol = Solution()
points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
ans = sol.maxPoints(points)
print("ans", ans)
