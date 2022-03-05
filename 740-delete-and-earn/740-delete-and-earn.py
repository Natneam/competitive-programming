class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0]*100001
        for num in nums:
            dp[num] += num
        
        for i in range(2, 100001):
            dp[i] = max(dp[i - 2] + dp[i], dp[i-1])
        
        return dp[10000]