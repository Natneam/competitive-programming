class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        
        def count1(x):
            count = 0 
            while x:
                count += x & 1
                x = x >> 1
            return count
        
        new_arr = [[count1(x), x] for x in arr]
        new_arr.sort()
        return [x[1] for x in new_arr]