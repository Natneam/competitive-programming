class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        
        def bin_search(index, value):
            start = index
            end = len(nums) - 1
            
            while start <= end:
                mid = (start + end) // 2
                if nums[mid] < value:
                    start = mid + 1
                elif nums[mid] > value:
                    end = mid - 1
                else:
                    return mid
            return -1
        
        nums.sort()
        visited = set()
        count = 0
        
        for i in range(len(nums)):
            vals = set()
            if nums[i] not in visited:
                vals.add(bin_search(i+1, nums[i] - k))
                vals.add(bin_search(i+1, k + nums[i]))
                visited.add(nums[i])
            
            if len(vals) == 1:
                if -1 not in vals:
                    count += 1
            elif len(vals) == 2:
                if -1 in vals:
                    count += 1
                else:
                    count += 2
        return count
    
    