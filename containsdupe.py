from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numSet = set()

        for num in nums:
            numSet.add(num)

        if len(numSet) != len(nums): return True

        return False
    
newSolution = Solution()

print(newSolution.containsDuplicate([1,2,3,3,4]))