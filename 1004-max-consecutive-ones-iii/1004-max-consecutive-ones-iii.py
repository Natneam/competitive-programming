class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        keep expanding 'end' unitl no more k left
        expand both when k is 0
        """
        start = 0
        ans = 0
        
        for end in range(len(nums)):
            if nums[end] == 0: 
                k -= 1
                
            if (k >= 0):
                ans = max(ans, end - start + 1)
            elif (k < 0):
                if(nums[start] == 0):
                    k += 1
                start += 1
        return ans