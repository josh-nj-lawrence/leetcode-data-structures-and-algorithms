class Solution:
    stack = []
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.process_string(s) == self.process_string(t)


    def process_string(self, x) -> str:
        self.stack = []
        for c in x:
            if self.stack:
                if c == "#":
                    self.stack.pop()
                else:
                    self.stack.append(c)
            elif c != "#":
                self.stack.append(c)
        return "".join(self.stack)

sol = Solution()
print(sol.backspaceCompare("y#fo##f","y#f#o##f"))

# Results: 53.7% time (35ms) 97.94% space (13.8MB)