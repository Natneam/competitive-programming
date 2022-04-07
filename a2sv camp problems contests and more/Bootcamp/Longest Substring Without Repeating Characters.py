# LINK TO THE PROBLEM => https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        firstPointer = 0   
        secondPointer = 0
        maxLength = 0
        if len(s) == 0:
            return 0
        while secondPointer < len(s):
            if len(s[firstPointer:secondPointer+1] ) > len(set(list(s[firstPointer:secondPointer+1]))):
                firstPointer += 1
            if maxLength < secondPointer - firstPointer + 1:
                maxLength = secondPointer - firstPointer + 1
            secondPointer += 1
        return maxLength