# LINK TO THE PROBLEM => https://leetcode.com/contest/weekly-contest-156/problems/get-equal-substrings-within-budget/

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        firstPointer = cost = maxWidth = i = 0
        while i < len(s) and firstPointer <= i:
            if cost + abs(ord(s[i]) - ord(t[i])) <= maxCost: 
                cost += abs(ord(s[i]) - ord(t[i]))
                maxWidth += 1
            else:
                cost -= abs(ord(s[firstPointer]) - ord(t[firstPointer])) 
                cost += abs(ord(s[i]) - ord(t[i]))
                firstPointer += 1
            i += 1
        return maxWidth
                
                