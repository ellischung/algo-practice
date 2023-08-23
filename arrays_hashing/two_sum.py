# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # add to hashmap as index : num
        # numMap = {}

        # for i, n in enumerate(nums):
        #     numMap[i] = n
        # print(numMap)

        # # check for complement in map
        # for i, n in enumerate(nums):
        #     complement = target - n
        #     if (complement in numMap.values()):
        #         for j in numMap:
        #             if (numMap[j] == complement) and (i != j):
        #                 return [i, j]
        # # no answer
        # return

        # ABOVE SOLUTION SUB-OPTIMAL

        prevMap = {}  # val -> index

        # check complement and add to map in one pass
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i # add to map after the check so we don't double count elements
    
print(Solution.twoSum(Solution, [1,3,5,6,4,2], 7))