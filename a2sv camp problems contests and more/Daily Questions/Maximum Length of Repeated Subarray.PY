# LINK TO THE PROBLEM => https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution:
    def findLength(self, A, B):
        dp = [[0 for __ in range(len(B) + 1)] for _ in range(len(A) + 1)]
        for i in range(len(A)-1, -1, -1):        
            for j in range(len(B)-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                
        maxLen = 0
        for row in dp:
            for item in row:
                maxLen = max(maxLen, item)
                
        return maxLen
