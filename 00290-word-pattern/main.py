class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        m1 = {}
        m2 = {}
        for i, letter in enumerate(pattern):
            word = words[i]
            if m1.get(letter) == None:
                m1[letter] = word
            else:
                if m1[letter] != word:
                    return False
            if m2.get(word) == None:
                m2[word] = letter
            else:
                if m2[word] != letter:
                    return False
        return True
