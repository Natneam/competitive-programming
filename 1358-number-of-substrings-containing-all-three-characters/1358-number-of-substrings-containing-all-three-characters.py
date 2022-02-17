class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        start, end = 0, 0
        elements = defaultdict(int, {s[0] : 1})
        counter = 0
        
        while end < len(s):
            if len(elements) >= 3:
                counter += len(s) - end
                elements[s[start]] -= 1
                if elements[s[start]] == 0:
                    del elements[s[start]]
                start += 1
            else:
                end += 1
                if end < len(s):
                    elements[s[end]] += 1
        return counter
        
            