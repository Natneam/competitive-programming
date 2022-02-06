class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        
        start = 0
        count = 0
        
        for num in nums:
            if freq[num] < 2:
                nums[start] = num
                freq[num] += 1
                start += 1
                count += 1
                
        return count