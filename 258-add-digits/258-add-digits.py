class Solution:
    def addDigits(self, num: int) -> int:
        curr_num = str(num)
        while len(curr_num) > 1:
            x = 0
            for i in curr_num:
                x += int(i)
            curr_num = str(x)
                
        
        return int(curr_num)