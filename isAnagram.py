# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            # # compare the lengths of both strings
            if len(s) != len(t):
                return False
            
            # # sort both strings
            # string1 = ''.join(sorted(s))
            # string2 = ''.join(sorted(t))

            # if string1 == string2:
            #     return True
            
            # return False

            # set up a hashmap
            # newMap = defaultdict(int)
            mapS = {}
            mapT = {}

            # put characters of first string in the map
            for i in range(len(s)):
                # newMap[char] += 1
                mapS[s[i]] = (mapS.get(s[i]) or 0) + 1
                mapT[t[i]] = (mapT.get(t[i]) or 0) + 1

            print(mapS)
            print(mapT)
            
            # compare the 2 maps 
            if mapS == mapT:
                return True
            
            # for char in t:
            #     if mapT.get(char) != mapS.get(char):
            #         return False

            return False
            # return True
    
newSolution = Solution()
print(newSolution.isAnagram("anagra", "nagaram"))        