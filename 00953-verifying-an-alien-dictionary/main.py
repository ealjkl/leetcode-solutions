from typing import List


def create_is_lower(order):
    d = {letter: index for index, letter in enumerate(order)}

    def is_lower(w1, w2):
        for i in range(min([len(w1), len(w2)])):
            diff = d[w1[i]] - d[w2[i]]
            if diff > 0:
                return False
            elif diff < 0:
                return True

        return len(w1) < len(w2)

    return is_lower


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        is_lower = create_is_lower(order)
        for i in range(1, len(words)):
            word1 = words[i - 1]
            word2 = words[i]
            if is_lower(word2, word1):
                return False
        return True


sol = Solution()
words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"
is_lower = create_is_lower(order)
# it is false meaning apple < app is false, meaning app < apple
ex = is_lower("app", "apple")
print("ex", ex)


ans = sol.isAlienSorted(words, order)
print("ans", ans)
