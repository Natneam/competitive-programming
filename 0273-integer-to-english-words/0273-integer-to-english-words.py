class Solution:
    def find(self, num):
        mapping = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine',
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen',
            20: 'Twenty',
            30: 'Thirty',
            40: 'Forty',
            50: 'Fifty',
            60: 'Sixty',
            70: 'Seventy',
            80: 'Eighty',
            90: 'Ninety'
        }
        
        res = []
        
        if len(str(num)) == 3:
            res.append(mapping[int(str(num)[0])] + " " + "Hundred")
            res = res + self.find(int(str(num)[1:]))
        else:
            if num in mapping:
                res.append(mapping[num])
            else:
                n = (num // 10)*10
                if n in mapping:
                    res.append(mapping[n])
                    res = res + self.find(int(str(num)[1:]))
        
        return res
                
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        
        ans = []
        while num:
            ans.append(" ".join(self.find(num % 1000)))
            num = num // 1000
        
        mapping = {
            0 : "",
            1 : "Thousand",
            2 : "Million",
            3 : "Billion"
        }
        res = []
        for i in range(len(ans)):
            if ans[i] != "":
                res.append(ans[i] + " " + mapping[i])
        
        return " ".join(reversed(res)).strip()
    