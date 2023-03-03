class Solution:
    def simplifyPath(self, path: str) -> str:
        """
            '/home/'
            '/../'
            '/home/./.foo/..//'
        """
        stack = []
        print(path.split("/"))
        for part in path.split("/"):
            if part == "..":
                if stack:
                    stack.pop()
            elif part == "." or not part:
                continue
            else:
                stack.append(part)
        return "/" + "/".join(stack)

sol = Solution()
print(sol.simplifyPath("//home/./.../.foo//.help//"))

# Results: 97.18% time (26ms) 32.18% space (13.9MB)