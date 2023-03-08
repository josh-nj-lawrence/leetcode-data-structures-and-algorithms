from typing import List
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i, j = 0, len(popped)
        stack = []
        for x in pushed:
            stack.append(x)
            while stack and i < j and stack[-1] == popped[i]:
                stack.pop()
                i += 1
        return i == j
    
# Results: 94.51% time (66ms) 88.63% space (14MB)