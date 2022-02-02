class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        def is_equal(p_arr, s_arr):
            return all(x[0] == x[1] for x in zip(p_arr, s_arr))
        
        p_arr = [0]*26
        s_arr = [0]*26
        
        for i in range(len(p)):
            p_arr[ord(p[i]) - ord('a')] += 1
            s_arr[ord(s[i]) - ord('a')] += 1
        
        ans = []
        i = 0
        while i < (len(s) - len(p)):
            if is_equal(p_arr, s_arr):
                ans.append(i)
            s_arr[ord(s[i]) - ord('a')] -= 1
            s_arr[ord(s[i + len(p)]) - ord('a')] += 1
            i += 1
        
        if is_equal(p_arr, s_arr):
            ans.append(i)
        
        return ans