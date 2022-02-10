class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter_prefix = Counter([0])
        
        prefix_sum = 0
        answer = 0
        
        for i in nums:
            prefix_sum += i
            answer += counter_prefix[prefix_sum - k]
            counter_prefix[prefix_sum] += 1
            
        return answer