#LINK TO THE PROBLEM => https://leetcode.com/explore/challenge/card/july-leetcoding-challenge-2021/608/week-1-july-1st-july-7th/3804/

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        frequency = dict()
        for item in arr:
            if item not in frequency:
                frequency[item] = 1
            else:
                frequency[item] += 1
        frequency = [(-freq, item) for item, freq in frequency.items()]
        
        frequency.sort()
        
        minimumSize = 0
        counter = 0
        
        for item in frequency:
            if counter < len(arr)/2:
                minimumSize += 1
                counter -= item[0]
            else:
                break
        return minimumSize
        
