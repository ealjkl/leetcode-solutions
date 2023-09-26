import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # assure that str1 is the shortest
        if len(str1) > len(str2):
            str1, str2 = str2, str1
        l1, l2 = len(str1), len(str2)
        l3 = l2 - l1
        if str1 != str2[:l1]:
            return ""
        d = math.gcd(l3, l2)
        if str2[l1:] != (l3//d)*str2[:d]:
            return ""
        return str2[:d]


sol = Solution()
ans = sol.gcdOfStrings("LEET", "CODE")
print("ans", ans)
