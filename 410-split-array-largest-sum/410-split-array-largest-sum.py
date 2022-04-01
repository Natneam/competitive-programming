class Solution:
    def find_sum(self, prefix_sum, start, end):
        return prefix_sum[end + 1] - prefix_sum[start]
    
    def helper(self, nums, prefix_sum, memo, start, m):
        if(m == 1): return self.find_sum(prefix_sum, start, len(nums) - 1)
        state = (start, m)
        if state in memo:
            return memo[state]
        
        best_ans = float('inf')
        for i in range(start, len(nums)):
            a = self.find_sum(prefix_sum, start, i)
            if a < best_ans:
                best_ans = min(best_ans, max(a, self.helper(nums, prefix_sum, memo, i+1, m -1)))
            else:
                break;
        memo[state] = best_ans
        
        return best_ans
    
    def splitArray(self, nums: List[int], m: int) -> int:
        prefix_sum = [0]
        for i in range(len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i])
        
        return self.helper(nums, prefix_sum, {}, 0, m)