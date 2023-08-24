# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # newMap = defaultdict(list)
    
        # for s in strs:
        #     # "eat" -> "aet"
        #     # "tea" -> "aet"
        #     # "ate" -> "aet"
        #     sortedS = "".join(sorted(s))
        #     newMap[sortedS].append(s)
        #     # { "aet" : [["eat"], ....]}

        # print(newMap.items())
        # print(newMap.values())
        # print(newMap.keys())
        # return newMap.values()
        # above algo is O(nlogn) because of sorting
        
        ans = defaultdict(list) # default empty list for hash map

        # for each str, create a key with alpha array ex: 1 e, 1 a, 1 t for the word "eat"
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s) # append str to the hashmap if it matches key
            # print(tuple(count))
            # python doesn't allow lists to be keys for hashmaps so we convert to tuple 
        return ans.values() # we return just the values
    
        # time complexity is O(m * n) where n is the length of the array and m is the largest character count of each str in the array
    
print(Solution.groupAnagrams(Solution, ["eat","tea","tan","ate","nat","bat"]))