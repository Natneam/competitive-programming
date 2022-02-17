class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        
        for i in nums:
            prefix_sum.append(prefix_sum[-1] + i % 2)
        
        counter = Counter()
        ans = 0
        
        for item in prefix_sum:
            if item - k in counter:
                ans += counter[item - k]
            counter[item] += 1
        
        return ans