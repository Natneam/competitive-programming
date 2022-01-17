class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_dict = {}
        p_dict = {}
        s = s.split()
        
        if len(s) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in p_dict and s[i] in s_dict:
                if s_dict[s[i]] != pattern[i] or p_dict[pattern[i]] != s[i]:
                    return False
            elif pattern[i] not in p_dict and s[i] not in s_dict:
                s_dict[s[i]] = pattern[i]
                p_dict[pattern[i]] = s[i]
            else:
                return False
        
        return True