class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def calc(a, b, c):
            count = [a,b,c].count("1")
            if count == 0:
                return "0", "0"
            if count == 1:
                return "1", "0"
            if count == 2:
                return "0", "1"
            if count == 3:
                return "1", "1"
            
        i, j = len(a) - 1, len(b) - 1
        carry = '0'
        res = []
        
        while i >= 0 or j >= 0:
            if i < 0:
                x, carry = calc(carry, b[j], 0)
                j -= 1
            elif j < 0:
                x, carry = calc(carry, a[i], 0)
                i -= 1
            else:
                x, carry = calc(carry, a[i], b[j])
                i -= 1
                j -= 1
            res.append(x)
        
        if carry != "0":
            res.append(carry)
        
        return "".join(reversed(res))