class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start = 0
        elements = defaultdict(int)
        counter = 0
        
        for end in range(len(s)):
            elements[s[end]] += 1
            while len(elements) == 3:
                counter += len(s) - end
                elements[s[start]] -= 1
                if elements[s[start]] == 0:
                    del elements[s[start]]
                start += 1
                
        return counter
        
            