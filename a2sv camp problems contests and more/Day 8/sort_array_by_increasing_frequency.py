# LINK TO THE PROBLEM => https://leetcode.com/problems/sort-array-by-increasing-frequency/

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = dict()
        for i in nums:
            if i not in freq.keys():
                freq[i] = 1
            else:
                freq[i] += 1
        temp_output = []
        for i,v in freq.items():
            temp_output.append([v,-i])
        
        temp_output.sort()
        
        output = []
        for i in temp_output:
            output += [-i[1]] * i[0]
        
        return output