class Solution:
    def myAtoi(self, s: str) -> int:
        possible_num = s.strip()
        val = ""
        
        if len(possible_num) == 0:
            return 0
        
        if possible_num[0] in "+-":
            val = "-" if possible_num[0] == "-" else ""
            possible_num = possible_num[1:]
                
        for i in range(len(possible_num)):
            if possible_num[i].isdigit():
                val += possible_num[i]
            else:
                break
        
        try:
            val = int(val)
            if val > (2**31) - 1:
                return (2**31) - 1
            elif val < -(2**31):
                return -(2**31)
            return val
        except:
            return 0