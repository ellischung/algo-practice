# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:
# Input: nums = [10,5,1,2,3,4,11,12]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:
# Input: nums = [0,3,7,2,5,8,1]
# Output: 9

# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        
        # sortedNums = sorted(nums)
        # longest = 1
        # current = 1

        # for i in range(1, len(nums)):
        #     if sortedNums[i] != sortedNums[i - 1]:
        #         if sortedNums[i] == sortedNums[i - 1] + 1:
        #             current += 1
        #         else:
        #             longest = max(longest, current)
        #             current = 1

        # return max(longest, current)
        if not nums:
            return 0
        
        numSet = set(nums)
        longest = 1

        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(longest, length)

        return longest



newSolution = Solution()
print(newSolution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))