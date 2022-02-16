class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        for num in nums:
            prefix_sum.append(num + prefix_sum[-1])
        records = defaultdict(int, {0 : 1})
        
        count = 0
        for i in range(1, len(prefix_sum)):
            if prefix_sum[i] - k in records:
                count += records[prefix_sum[i] - k]
            records[prefix_sum[i]] += 1
        
        return count