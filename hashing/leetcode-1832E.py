class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = set()
        for x in sentence:
            if x not in seen:
                seen.add(x)
            elif len(seen) == 26:
                return True
        return True if len(seen) == 26 else False
    
solution = Solution()
print(solution.checkIfPangram("thequickbrownfoxjumpsoverthelasdfzydog"))