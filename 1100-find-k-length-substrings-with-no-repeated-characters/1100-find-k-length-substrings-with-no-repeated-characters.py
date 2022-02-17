class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        """
        have a window sized k
        record all the unique elements in a set, 
        if the length of the set is equals to k, increment the counter
        else move the window and reaptedly cross chek the size of the set with k
        
        """
        elements = Counter(s[:k])
        
        counter = 0
        if len(elements) == k:
            counter += 1
        
        for i in range(len(s)-k):
            elements[s[i]] -= 1
            if elements[s[i]] == 0:
                del elements[s[i]]
            
            elements[s[i+k]] += 1
            
            if len(elements) == k:
                counter += 1
        
        return counter
            
            
        