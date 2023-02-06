from collections import defaultdict
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = defaultdict(int)
        x,y = 0,0
        visited[(x,y)] = 1
        for p in path:
            if p == "N":
                y += 1
            elif p == "S":
                y -= 1
            elif p == "W":
                x -= 1
            else:
                x += 1
            if visited[(x,y)] == 1:
                return True
            visited[(x,y)] += 1
            print(visited)
        return False

solution = Solution()
print(solution.isPathCrossing("NESWW"))

# Results: 78.77% time (31ms) 99.81% space (13.8MB)