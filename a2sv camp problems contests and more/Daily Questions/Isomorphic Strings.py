#LINK TO THE PROBLEM => https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapOfChars = {}
        values = set()
        
        for i in range(len(s)):
            if s[i] in mapOfChars:
                if mapOfChars[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in values:
                    mapOfChars[s[i]] = t[i]
                    values.add(t[i])
                else:
                    return False
        return True
