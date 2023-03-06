from typing import List
from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2:
            return None

        stack = []
        stack.append(nums2[0])
        hashmap = defaultdict()

        for i in range(1,len(nums2)):
            while stack and nums2[i] > stack[-1]:
                hashmap[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while stack:
            hashmap[stack.pop()] = -1

        return [hashmap[nums1[i]] for i in range(len(nums1))]
    
sol = Solution()
print(sol.nextGreaterElement([4,1,2],[1,3,4,2]))

# Results: 97.14% time (41ms) 8.74% space (14.2MB)