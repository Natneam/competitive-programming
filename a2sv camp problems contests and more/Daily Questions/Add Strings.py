# LINK TO THE PROBLEM => https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        longest_num_length = len(num1) if len(num1) >= len(num2) else len(num2)
        index = -1
        carry = 0
        string_sum = ""
        
        while index >= -longest_num_length:            
            if len(num1) >= abs(index):
                carry += int(num1[index])
                
            if len(num2) >= abs(index):
                carry += int(num2[index])

            string_sum = str(carry % 10) + string_sum
            
            carry = (carry - carry%10)//10
            
            index -= 1
            
        return str(carry) + string_sum if carry != 0 else string_sum
            
            