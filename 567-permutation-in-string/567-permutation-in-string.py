class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)< len(s1):
            return False
        
        def is_equal(s1_count, s2_count):
            for i in range(len(s1_count)):
                if s1_count[i] != s2_count[i]:
                    return False
            return True
        
        s1_count = [0]*26
        s2_count = [0]*26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        
        s1_len = len(s1)
        
        for i in range(s1_len, len(s2)):
            if is_equal(s1_count, s2_count):
                return True
            s2_count[ord(s2[i - s1_len]) - ord('a')] -= 1
            s2_count[ord(s2[i]) - ord('a')] += 1        
        if is_equal(s1_count, s2_count):
            return True
            
        return False