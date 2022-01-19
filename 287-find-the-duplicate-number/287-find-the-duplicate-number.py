class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n1 = nums[0]
            n2 = nums[n1]
            
            if n1 == n2:
                return n1
            
            nums[0]  = n2
            nums[n1] = n1
        
        return -1
            