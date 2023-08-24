from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sortedStrs = sorted(strs)
        # print(sortedStrs)
        newMap = defaultdict(list)
    
        for s in strs:
            # "eat" -> "aet"
            # "tea" -> "aet"
            # "ate" -> "aet"
            sortedS = "".join(sorted(s))
            newMap[sortedS].append(s)
            # { "aet" : [["eat"], ....]}

        print(newMap.items())
        print(newMap.values())
        print(newMap.keys())
        return newMap.values()

newSolution = Solution()
print(newSolution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))