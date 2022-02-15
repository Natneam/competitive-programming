class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        set of values 
        add the first two values
        try to expand the second pointer as long as I have the only two elements in the set
        if the set has 3(more than 2) elements start moving the first pointer
        set = {3, 4, 5}
        max_window = 2
        [0, 1, 2, 2, 3 , 3, 4, 5]
                            |  |
        """
        if len(fruits) <= 2:
            return len(fruits)
        
        elements = defaultdict(int)
        elements[fruits[0]] += 1
        elements[fruits[1]] += 1
        start = 0
        ans = 2
        
        for i in range(2, len(fruits)):
            elements[fruits[i]] += 1
            
            if len(elements) > 2:
                elements[fruits[start]] -= 1
                if elements[fruits[start]] == 0:
                    del elements[fruits[start]]
                start += 1
            else:
                ans = max(ans, i - start + 1)
                
        return ans