class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        def is_overlap(interval1, interval2):
            intervals = [interval1, interval2]
            intervals.sort()
            return intervals[1][0] <= intervals[0][1]
            
        ans = 0
        
        first_window_sum = sum(nums[:firstLen])
        for i in range(len(nums) - firstLen + 1):
            second_window_sum = sum(nums[:secondLen])
            for j in range(len(nums) - secondLen + 1):
                if not is_overlap([i, i + firstLen - 1], [j, j + secondLen - 1]):
                    ans = max(ans, sum(nums[i:i+firstLen]) + sum(nums[j:j+secondLen]))
                second_window_sum += (nums[j + secondLen - 2] - nums[j])
            first_window_sum += (nums[i + firstLen - 2] - nums[i])
        return ans