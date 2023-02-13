class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0 : 1}
        running_sum = 0
        for num in nums:
            running_sum += num
            x = running_sum % k
            freq[x] = freq.get(x, 0) + 1
            
        res = 0
        for k in freq:
            N = freq[k]
            res += (N * (N - 1)) // 2
        return res