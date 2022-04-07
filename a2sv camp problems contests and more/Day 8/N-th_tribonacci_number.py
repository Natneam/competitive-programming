# LINK TO THE PROBLEM => https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        # if n == 0:
        #     return 0
        # elif n == 1 or n == 2:
        #     return 1
        # else:
        #     return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        val0 = 0
        val1 = 1
        val2 = 1
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            counter = 3
            temp_sum = val0 + val1 + val2
            while counter <= n:
                temp_sum = val0 + val1 + val2
                val0 = val1
                val1 = val2
                val2 = temp_sum
                counter += 1
            return temp_sum