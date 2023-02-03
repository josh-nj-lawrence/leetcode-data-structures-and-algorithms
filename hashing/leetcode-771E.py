from collections import defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Meant to be a hashing problem but using jewel_type as a set would be fast and implement if stone in jewel_type instead
        jewel_types = defaultdict(int)
        ans = 0
        for jewel in jewels:
            jewel_types[jewel] +=1 
        for stone in stones:
            if jewel_types[stone] != 0:
                ans += 1
        return ans

# Results: 76.46% time (32 ms) 52.82% space (13.8MB)