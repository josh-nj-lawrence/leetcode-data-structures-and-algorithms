class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = set()
        for l in s:
            if l in letters:
                return l
            letters.add(l)
        return " "