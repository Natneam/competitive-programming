class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        """
        start = 0
        diff = the disffeence between the first two elements
        end = 2
        
        move the second pointer as long as the diff hold
        when it doesn't or the array ends -> calcualte the amount of the subarry which are arthmetic slice
        
        subarry wirh size >= 3 -> (n - 1)(n - 2) / 2
        """
        if len(nums) < 3:
            return 0
        
        start = 0
        diff = nums[1] - nums[0]
        ans = 0
        
        for end in range(2, len(nums)):
            if nums[end] - nums[end - 1] != diff:
                n = end - start
                if n > 2:
                    ans += int((n - 1)*(n - 2) / 2)
                
                start = end - 1
                diff = nums[end] - nums[start]
        
        n = end - start + 1
        if n > 2:
            ans += int((n - 1)*(n - 2) / 2)
        
        return ans