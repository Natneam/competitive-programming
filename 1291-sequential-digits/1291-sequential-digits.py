class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        """
        find the first valid number which is greater than 'low'

        generate all the possible valid numbers using the number which is greater than lowest valid number until it is greater thna the 'high' value
        
        #algo for the generate function
        n = 3
        return all valid combination which has n digits
        I'll add all the numbers which are between the high and low number
        after that
        I'll increamne n by one and do the same thing again
        """       
        def generate(n):
            sequence = [1, 2, 3, 4, 5 ,6, 7, 8, 9]
            ans = []
            for i in range(10-n):
                ans.append(int("".join(list(map(str, sequence[i:n+i]))))) #TODO: add the numbers instead
            
            return ans
        
        ans = []
        num_length = len(str(low))
        
        vals = generate(num_length)
        
        while len(vals) > 0:
            for val in vals:
                if val > high:
                    return ans
                elif val >= low:
                    ans.append(val)
            num_length += 1  
            vals = generate(num_length)
            
        return ans
                    
        