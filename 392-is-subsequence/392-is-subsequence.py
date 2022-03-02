class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        find the first occurance of the first letter in t
        then call do the same for the remaining s and t
        """
        
        def find(i, j):
            nonlocal s, t
            
            if i == len(s):
                return True
            
            for k in range(j, len(t)):
                if t[k] == s[i]:
                    return find(i+1, k+1)
            return False
        
        return find(0, 0)
            