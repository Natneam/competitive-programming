class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """
        generate all combination sum for the two of the arrays pair
        do two sum on them and count the valids(summed to zeros)
        
        """
        pair1 = defaultdict(int)
        pair2 = defaultdict(int)
        
        for i in nums1:
            for j in nums2:
                pair1[i + j] += 1
        for i in nums3:
            for j in nums4:
                pair2[i + j] += 1
        
        ans = 0
        for i in pair1:
            if -i in pair2:
                ans += pair1[i] * pair2[-i]
        
        return ans
        
        