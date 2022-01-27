class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def change_to_bits(number):
            b = bin(number)[2:]
            return "0"*(32 - len(b)) + b
        
        trie = {}
        # add to the trie                                                                              
        for number in nums:
            bits = change_to_bits(number)
            node = trie
            for b in bits:
                if b not in node:
                    node[b] = {}
                node = node[b]
        
        #calcualte the value
        mapper = {"1" : "0", "0" : "1"}
        ans = 0
        for number in nums:
            bits = change_to_bits(number)
            node = trie
            value = ""
            i = 0
            while i < len(bits):
                complmenent = mapper[bits[i]] 
                if complmenent in node:
                    node = node[complmenent]
                    value += "1"
                else:
                    node = node[bits[i]]
                    value += "0"
                i+=1
                
            ans = max(ans, int(value, 2))
        return ans
        
        