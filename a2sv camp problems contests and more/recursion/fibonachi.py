# LINK TO THE PROBLEM => https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        num1 = 0
        num2 = 1
        counter = 1
        if n == 0:
            return 0
        while counter < n:
            temp = num1
            num1 = num2
            num2 = num2 + temp
            counter += 1
        return num2