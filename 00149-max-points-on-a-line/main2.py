from typing import List
import math


def reduce_fraction(a, b):
    gcd = math.gcd(a, b)
    return (a//gcd, b//gcd)


def find_coef(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    A = y2 - y1
    B = x1 - x2
    C = y1*(x2 - x1) + x1*(y1 - y2)
    return (A, B, C)


# def reduce_coef(A, B, C):
#     return (reduce_fraction(B, A), reduce_fraction(C, A))

def reduce_coef(A, B, C):
    gcd = math.gcd(A, B, C)
    return (A//gcd, B//gcd, C//gcd)


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if (len(points) <= 2):
            return len(points)
        d = {}
        for i in range(len(points)):
            point1 = points[i]
            for j in range(i + 1, len(points)):
                point2 = points[j]
                key = reduce_coef(*find_coef(point1, point2))
                if (d.get(key) is None):
                    d[key] = {tuple(point1), tuple(point2)}
                else:
                    d.get(key, set()).add(tuple(point1))
                    d.get(key, set()).add(tuple(point2))
        d2 = {key: value for key, value in d.items() if len(value) == 38}
        for key, value in d2.items():
            print(key, value)
            print()
        return max([len(line) for line in d.values()])


sol = Solution()
# points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
# points = [[0, 0], [1, -1], [1, 1]]
points = [[7, 3], [19, 19], [-16, 3], [13, 17], [-18, 1], [-18, -17], [13, -3], [3, 7], [-11, 12], [7, 19], [19, -12], [20, -18], [-16, -15], [-10, -15], [-16, -18], [-14, -1], [18, 10], [-13, 8], [7, -5], [-4, -9], [-11, 2], [-9, -9], [-5, -16], [10, 14], [-3, 4], [1, -20], [2, 16], [0, 14], [-14, 5], [15, -11], [3, 11], [11, -10], [-1, -7], [16, 7], [1, -11], [-8, -3], [1, -6], [19, 7], [3, 6], [-1, -2], [7, -3], [-6, -8], [7, 1], [-15, 12], [-17, 9], [19, -9], [1, 0],
          [9, -10], [6, 20], [-12, -4], [-16, -17], [14, 3], [0, -1], [-18, 9], [-15, 15], [-3, -15], [-5, 20], [15, -14], [9, -17], [10, -14], [-7, -11], [14, 9], [1, -1], [15, 12], [-5, -1], [-17, -5], [15, -2], [-12, 11], [19, -18], [8, 7], [-5, -3], [-17, -1], [-18, 13], [15, -3], [4, 18], [-14, -15], [15, 8], [-18, -12], [-15, 19], [-9, 16], [-9, 14], [-12, -14], [-2, -20], [-3, -13], [10, -7], [-2, -10], [9, 10], [-1, 7], [-17, -6], [-15, 20], [5, -17], [6, -6], [-11, -8]]
ans = sol.maxPoints(points)
print("ans", ans)
