class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        d = set()
        for i in nums:
            if i > 0:
                d.add(i)
        
        for i in range(1, len(nums)+2):
            if i not in d:
                return i