class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        keep expanding 'end' unitl no more k left
        expand both when k is 0
        """
        start = 0
        
        for end in range(len(nums)):
            k -= 1 - nums[end]
                
            if (k < 0):
                if(nums[start] == 0):
                    k += 1
                start += 1
                
        return end - start + 1