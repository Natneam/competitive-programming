# LINK TO THE PROBLEM => https://leetcode.com/problems/minimum-operations-to-make-array-equal/

class Solution:
    def minOperations(self, n: int) -> int:        
        answer = 0
        for i in range(int(n/2)):
            answer += n - 1 - 2*i
        return answer
