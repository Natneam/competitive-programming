class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) <= len(b):
            a = "0" * (len(b)-len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b
        
        def add_bits(b1, b2, reminder='0'):
            bits = [b1, b2, reminder]
            if bits.count('0') == 3:
                return '0', '0'
            elif bits.count('0') == 2:
                return '1', '0'
            elif bits.count('0') == 1:
                return '0', '1'
            else:
                return '1', '1'
        
        
        
        reminder = '0'
        ans = ''
        pointer = len(a) - 1
        
        while pointer >= 0:
            summation, reminder = add_bits(a[pointer], b[pointer], reminder)
            # print(summation, reminder)
            ans += summation
            
            pointer -= 1
        
        ans = "".join(reversed(ans if reminder == '0' else ans + reminder))
        
        return  ans