class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        res = curr = 0
        for num in nums:
            if num != 0 and num > curr:
                res += 1
                curr = num
        
        return res